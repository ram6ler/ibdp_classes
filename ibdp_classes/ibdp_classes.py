#! python3

import re, sys, traceback
from typing import Generic, TypeVar
from contextlib import redirect_stdout
from io import StringIO

T = TypeVar("T")


class _Base(Generic[T]):
    def __init__(self, *elements: T) -> None:
        self._elements = list(elements)

    def __str__(self) -> str:
        if len(self._elements) and isinstance(self._elements[0], str):
            template = '"[ELEMENT]"'
        else:
            template = "[ELEMENT]"
        elements = (
            "{ "
            + ", ".join(template.replace("[ELEMENT]", str(x)) for x in self._elements)
            + " }"
            if self._elements
            else "(empty)"
        )
        return f"{type(self).__name__} {elements}"


class _KnowsIfEmpty(_Base[T]):
    def isEmpty(self) -> bool:
        """Returns whether the structure contains any elements."""
        return not self._elements


class Array(_Base[T]):
    """A basic array structure that only allows random access."""

    def __init__(self, *elements: T) -> None:
        super().__init__(*elements)

    def __setitem__(self, index: int, value: T) -> None:
        if isinstance(index, int):
            if 0 <= index < len(self._elements):
                self._elements[index] = value
            else:
                raise IndexError("Array index out of bounds.")
        else:
            raise IndexError("Non integer Array index.")

    def __getitem__(self, index: int) -> T:
        if isinstance(index, int):
            if 0 <= index < len(self._elements):
                return self._elements[index]

            raise IndexError("Array index out of bounds.")
        raise IndexError("Non integer Array index.")


class Collection(_KnowsIfEmpty[T]):
    """A basic collection class that only supports methods `hasNext`,
    `getNext`, `resetNext`, `addItem` and `isEmpty`."""

    def __init__(self, *elements: T) -> None:
        super().__init__(*elements)
        self.index = 0

    def addItem(self, element: T) -> None:
        """Adds element `element` at the current index."""
        self._elements = (
            self._elements[0 : self.index] + [element] + self._elements[self.index :]
        )
        self.index += 1

    def getNext(self) -> T:
        """Returns the next item in the collection."""
        if self.index < len(self._elements):
            element = self._elements[self.index]
            self.index += 1
            return element

        raise Exception("No elements remaining.")

    def resetNext(self) -> None:
        """Resets the iteration index."""
        self.index = 0

    def hasNext(self) -> bool:
        """Returns whether there are any more items."""
        return self.index < len(self._elements)


class Stack(_KnowsIfEmpty[T]):
    """A basic collection class that only supports methods `push`,
    `pop` and `isEmpty`"""

    def __init__(self, *elements: T) -> None:
        super().__init__(*elements)

    def push(self, element: T) -> None:
        """Adds element `element` to the top of the stack."""
        self._elements.append(element)

    def pop(self) -> T:
        """Removes and returns the item at the top of the stack."""
        if self._elements:
            return self._elements.pop()

        raise Exception("Tried popping an empty stack.")


class Queue(_KnowsIfEmpty[T]):
    """A basic collection class that only supports methods `enqueue`,
    `dequeue` and `isEmpty`"""

    def __init__(self, *elements: T) -> None:
        super().__init__(*elements)

    def enqueue(self, element: T) -> None:
        """Adds element `element` to the back of the queue."""
        self._elements.append(element)

    def dequeue(self) -> T:
        """Removes and returns the element at the front of the queue."""
        if self._elements:
            x, *self._elements = self._elements
            return x

        raise Exception("Attempted to dequeue an empty queue.")


class Pseudocode:
    """A simple IBDP pseudocode interpreter."""

    def __init__(self, code: str) -> None:
        self.code = code
        lines = [line for line in code.split("\n")]
        r_logic = re.compile(r" AND | OR | NOT ")
        r_if = re.compile(r"if +(.*) +then")
        r_else = re.compile(r"else")
        r_while = re.compile(r"loop +while +(.*)")
        r_for = re.compile(r"loop +([A-Z][A-Z_0-9]*) +from +([^ ]+) +to +(.+)")
        r_end = re.compile(r"end +(.+)")
        r_input_type = re.compile(r"input +([A-Z][A-Z_0-9]*) +as +(.*)")
        r_input = re.compile(r"input +([A-Z][A-Z_0-9]*)")
        r_output = re.compile(r"output +(.*)")
        r_function = re.compile(r"function +([A-Z][A-Z_0-9]*)\((.*)\)")
        r_procedure = re.compile(r"procedure +([A-Z][A-Z_0-9]*)\((.*)\)")
        r_new = re.compile(r"new +(Array|Collection|Queue|Stack) *\(")
        r_string = re.compile(r'"([^"]*)"')
        r_string_index = re.compile(r"<<<([0-9]+)>>>")
        r_lower = re.compile(r"[a-z]+")
        r_equals = re.compile(r"==+")

        # Allowed lowercase in the generated Python.
        allowed_lower = [
            "and",
            "or",
            "not",
            "return",
            "if",
            "else",
            "while",
            "input",
            "int",
            "float",
            "isEmpty",
            "addItem",
            "resetNext",
            "getNext",
            "hasNext",
            "push",
            "pop",
            "enqueue",
            "dequeue",
            "True",
            "False",
        ]

        # Code structure stack.
        stack = list[str]()

        # Replace special symbols and work around IB's choice to use the same
        # symbol for instantiation and equality.
        def special(line: str) -> str:
            for c, r in {
                "≠": "!=",
                "≤": "<=",
                "≥": ">=",
                "=": "==",
                "!==": "!=",
                "<==": "<=",
                ">==": ">=",
            }.items():
                line = line.replace(c, r)
            if m := r_equals.match(line):
                line = line.replace(m.group(0), "==")
            return line

        def to_python(line_number: int, line: str) -> str:
            padding = "  " * len(stack)
            while m := r_logic.match(line):
                line = line.replace(m.group(1), m.group(1).lower())
            for s, r in {
                "//": "#",
                " div ": " // ",
                " mod ": " % ",
                "true": "True",
                "TRUE": "True",
                "false": "False",
                "FALSE": "False",
            }.items():
                line = line.replace(s, r)

            while r_new.search(line):
                line = re.sub(r_new, r"\1(", line)

            if m := r_if.match(line):
                stack.append("if")
                check = line.split("then")
                if len(check) != 2 or check[1].strip():
                    sys.stderr.write(
                        f"* Error in line {line_number + 1}: '{line}'\n  Should be if the form: if [condition] then"
                    )
                    exit(-1)
                return special(f"{padding}if {m.group(1)}:")

            if r_else.match(line):
                if line != "else":
                    sys.stderr.write(
                        f"""* Error in line {line_number + 1}: '{line}'\n  Keyword 'else' should be on its own\n"""
                    )
                    exit(-1)
                return f"{padding[0:-2]}else:"

            if m := r_while.match(line):
                stack.append("loop")
                return special(f"{padding}while {m.group(1)}:")

            if m := r_for.match(line):
                stack.append("loop")
                return f"{padding}for {m.group(1)} in range({m.group(2)}, {m.group(3)} + 1):"

            if m := r_end.match(line):
                pop = stack.pop()
                if pop != m.group(1):
                    sys.stderr.write(
                        f"* Error in line {line_number + 1}: '{line}'\n  Expecting: end {pop}\n"
                    )
                    exit(-1)
                return ""

            if m := r_input_type.match(line):
                return f"{padding}{m.group(1)} = {m.group(2)}(input())"

            if m := r_input.match(line):
                return f"{padding}{m.group(1)} = input()"

            if m := r_output.match(line):
                return f"{padding}print({m.group(1)})"

            if m := r_function.match(line):
                stack.append("function")
                return f"{padding}def {m.group(1)}({m.group(2)}):"

            if m := r_procedure.match(line):
                stack.append("procedure")
                return f"{padding}def {m.group(1)}({m.group(2)}):"

            # Remove strings.
            strings = list[str]()
            while m := r_string.match(line):
                i = len(strings)
                line = line.replace(m.group(1), f"<<<{i}>>>")

            start = 0
            while m := r_lower.match(line, start):
                start = m.end()
                if m.group(0) not in allowed_lower:
                    sys.stderr.write(
                        f"* Error in line {line_number + 1}: {line}\n  Not defined: {m.group(0)}\n"
                    )
                    exit(-1)

            # Replace strings.
            while m := r_string_index.match(line):
                i = int(m.group(1))
                line = line.replace(f"<<<{i}>>>", strings[i])

            return f"{padding}{line}"

        self.python = "\n".join(
            to_python(line_number, line.strip())
            for line_number, line in enumerate(lines)
        )

        if len(stack) > 0:
            sys.stderr.write(
                f"""* Error: incomplete structures; missing: {', '.join(f"end {s}" for s in stack)}\n"""
            )
            exit(-1)

    def __call__(self, access: dict[str, object] = {}) -> str:
        env = {**globals(), **locals(), **access}
        s = StringIO()
        with redirect_stdout(s):
            try:
                exec(self.python, env, env)
            except:
                error_lines = traceback.format_exc().split("\n")
                # Hack: "<string>", line 10
                r_line = re.compile(r'.*"<string>", line ([0-9]+).*')

                line_number = -1
                for line in error_lines:
                    if m := r_line.match(line):
                        line_number = int(m.group(1))
                        linebreak = "\n"
                        print(
                            f"""* Error in line {line_number}:
    {self.code.split(linebreak)[line_number - 1].strip()}
    {error_lines[-2]}
    """
                        )
        return s.getvalue()

    def __str__(self) -> str:
        return self.code
