import sys
from .ibdp_classes import Pseudocode


def run():
    def help():
        print(
            """
To use:

  python -m ibdp_classes [options] filename

Options:

  -md  Output markdown.
  -py  Output intermediate Python code.

"""
        )
        exit(0)

    if len(sys.argv) < 2:
        help()

    md = "-md" in sys.argv
    py = "-py" in sys.argv

    file_name = sys.argv[-1]

    try:
        with open(file_name) as f:
            lines = [line for line in f]
    except:
        help()

    code = "".join(lines)
    pc = Pseudocode(code)

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
