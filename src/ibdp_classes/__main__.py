import sys
from .ibdp_classes import (
    Array,
    Collection,
    Pseudocode,
    Queue,
    Stack,
)


def run():
    def help():
        print(
            """
To use:

  python -m ibdp_classes [options] filename

Options:

  -md           Output markdown.
  -py           Output intermediate Python code.
  -defs [file]  Include definitions implemented in Python.

"""
        )
        exit(0)

    if len(sys.argv) < 2:
        help()

    md = "-md" in sys.argv
    py = "-py" in sys.argv

    if "-defs" in sys.argv:
        i = sys.argv.index("-defs") + 1
        if i == len(sys.argv):
            help()
        try:
            with open(sys.argv[i]) as f:
                defs = f.read()
        except:
            print("Check option -def; example: -def defs.py")
            help()
    else:
        defs = ""

    file_name = sys.argv[-1]

    try:
        with open(file_name) as f:
            lines = [line for line in f]
    except:
        help()

    code = "".join(lines)
    pc = Pseudocode(code)
    pc.python = f"{defs}\n{pc.python}"

    # If it is interactive, just run (ignores options).
    if any(["input " in line for line in lines]):
        exec(pc.python)
        exit(0)

    if md:
        print("```")
        print(pc)
        print("```\n")

    if md and py:
        print("```python")
    if py:
        print(pc.python)
    if md and py:
        print("```\n")
    if py and not md:
        print("\n\n")

    if md:
        print("Output:\n\n```")
    print(pc())
    if md:
        print("```")


if __name__ == "__main__":
    run()
