# IBDP Computer Science Pseudocode Classes

The IB Computer Science documents, *Approved notation for developing pseudocode* and *Pseudocode in Examinations*, describe pseudocode and a set of limited-functionality *array*, *collection*, *stack* and *queue* data structure classes that may come up and be used in exams.

This is a simple Python implementation of an IB pseudocode interpreter and the above restrictive classes, which can be used in programming activities to help familiarize students with the pseudocode and classes.

Under the hood, the classes are simple wrappers over a Python list and the interpreter simply runs some perfunctory tests, translates pseudocode into Python (with a heavy, ugly accent) and then does its best to execute the translation and report helpful error messages. 

You can submit [issues and requests here](https://github.com/ram6ler/ibdp_classes/issues).


## Interpreting IB pseudocode

We can use the library to interpret pseudocode. For example:

`example.pseudocode`
```text
output "Collection..."
ITEMS = new Collection(1, 2, 3)
ITEMS.resetNext()
loop while ITEMS.hasNext()
    X = ITEMS.getNext()
    output "X =", X
end loop
```

To interpret:

```
python -m ibdp_classes example.pseudocode
```

Output:

```txt
Collection...
X = 1
X = 2
X = 3
```

We can also interpret IB pseudocode from within a Python script. For example:

```python
import ibdp_classes as ib

code = """
output "Array..."
XS = new Array(1, 2, 3, 4, 5)
N = 5
loop I from 0 to N - 1
    output "xs[", I, "] = ", XS[I]
end loop
"""

script = ib.Pseudocode(code)
output = script()
print(output)
```

Output:

```txt
Array...
xs[ 0 ] =  1
xs[ 1 ] =  2
xs[ 2 ] =  3
xs[ 3 ] =  4
xs[ 4 ] =  5
```

If we would like to give the pseudocode access to already defined variables or functions, we can pass the definitions via a dictionary:

```python
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
```

Example output:

```text
1 : 5
2 : 1
3 : 9
4 : 9
5 : 7
6 : 0
7 : 4
8 : 1
9 : 7
10 : 0
```

## Additions to IB pseudocode

### `function` and `procedure`

In exams, IB pseudocode typically uses `output` to display results, and doesn't explicitly define functions or procedures. These are often useful constructs in programming tutorials, however, so I have also implemented `function` (to define expressions) and `procedure` (to define statements) structures. For example:

```text
function CONTAINS(NEEDLE, HAYSTACK, N)
    // Where NEEDLE is a string, HAYSTACK is an Array
    // of strings, and N is the length of HAYSTACK.
    FOUND = false
    loop K from 0 to N-1
        if HAYSTACK[K] = NEEDLE then
            FOUND = true
        end if
    end loop
    return FOUND
end function

HAYSTACK = new Array(20, -3, 5, 7, 2, 13, 12, 19)
output "HAYSTACK:", HAYSTACK

output "5 is in HAYSTACK?"
output CONTAINS(5, HAYSTACK, 8)

output "4 is in HAYSTACK?"
output CONTAINS(4, HAYSTACK, 8)
```

Output:

```
HAYSTACK: Array { 20, -3, 5, 7, 2, 13, 12, 19 }
5 is in HAYSTACK?
True
4 is in HAYSTACK?
False
```

### Input types using `as`

In IBDP pseudocode, the keyword `input` is used to generically collect input from the user, and context is used to determine whether the input should be interpreted as a string, integer or floating point number. I have added `as int` and `as float` as appendages to the input statement for when we want to be explicit.

For example:

```
output "Input an integer."
input COUNT as int

if COUNT mod 2 = 0 then
    output COUNT, "is even..."
else
    output COUNT, "is odd..."
end if
```

## Using the classes within Python scripts

The classed defined by IB can be used directly in Python scripts. For example:

```python
from ibdp_classes import Array

def contains(needle: int, haystack: Array[int], n: int) -> bool:
    found = False
    for k in range(n):
        if haystack[k] == needle:
            print("Found!")
            found = True
    return found

haystack = Array(20, -3, 5, 7, 2, 13, 12, 19)
print("haystack:", haystack)

print("5 is in haystack?")
print(contains(5, haystack, 8))

print("4 is in haystack?")
print(contains(4, haystack, 8))
```

