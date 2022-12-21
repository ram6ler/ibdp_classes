from random import random
from math import floor
import ibdp_classes as ib

code = """
loop I from 1 to 10
    output I, ":", FLOOR(10 * RANDOM())
end loop
"""

script = ib.Pseudocode(code)
output = script({"FLOOR": floor, "RANDOM": random})
print(output)
