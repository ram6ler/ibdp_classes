import sys
import pathlib
from .ibdp_classes import *


if __name__ == "__main__":

    def help():
        print(
            """
To use:

  python -m ibdp_classes [options] filename

Options:

  -md                              Output markdown.
  -py                              Output intermediate Python code (for debugging).
  -defs [Python file]              Include bespoke definitions implemented in Python.
  -ext 'extension1 extension2 ...' Add extended functionality.
                                   Extensions available:
                                      strings      String manipulation; substrings.
                                      turtle       Turtle graphics.
                                      math         Common math constants and functions.
                                      bits         Bit manipulation.

"""
        )
        exit(0)

    if len(sys.argv) < 2:
        help()

    md = "-md" in sys.argv
    py = "-py" in sys.argv

    defs = ""
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

    if "-ext" in sys.argv:
        i = sys.argv.index("-ext") + 1
        if i == len(sys.argv):
            help()
        extensions = [
            extension.strip()
            for extension in sys.argv[i].replace("'", "").replace('"', "").split(" ")
        ]
    else:
        extensions = list[str]()

    file_name = sys.argv[-1]

    lines = list[str]()
    try:
        with open(file_name) as f:
            lines = [line for line in f]
    except:
        help()

    code = "".join(lines)
    pc = Pseudocode(code)
    # TODO: add extension code.
    path = pathlib.Path(__file__).parent.parent
    for extension in extensions:
        try:
            with open(f"{path}/extensions/{extension}_defs.py") as f:
                pc.python = f"{f.read()}\n{pc.python}"
        except:
            print(f"Unknown extension '{extension}'.")
            help()

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
