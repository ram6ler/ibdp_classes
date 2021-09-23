# IBDP Computer Science Pseudocode Classes

The IB Computer Science document, *Pseudocode in Examinations*, describes a set of limited-functionality *array*, *collection*, *stack* and *queue* data structure classes that students may expect to encounter or use in exam pseudocode.

This is a simple Python implementation of these restricted classes, which can be used in programming activities to help familiarize students with these classes.

Classes are very simple wrappers over a Python list. The focus is to artificially restrict functionality rather than implement particularly useful or efficient structures*

The basic classes are:

## `Array`

A basic array class that only supports random access via indices (for example, it doesn't support dynamically determining or changing the length of the array).

### Example IB pseudocode:

```text
function CONTAINS(NEEDLE, HAYSTACK, N)
    // Where NEEDLE is a string, HAYSTACK is an Array
    // of strings, and N is the length of HAYSTACK.
    FOUND = false
    loop K from 0 to N-1
        if HAYSTACK[k] = NEEDLE then
            output "Found!"
            FOUND = true
        end if
    end loop
    return FOUND
end function
```

### Literal Python translation:

```python
from ibdp_classes import Array

def contains(needle: str, haystack: Array[str], n: int) -> bool:
    found = False
    for k in range(n):
        if haystack[k] == needle:
            print("Found!")
            found = True
    return found
```

## `Collection`

A basic collection class that only supports methods `hasNext`, `getNext`, `resetNext` and `addItem`.

### Example IB pseudocode:

```text
function ITEMS_DIVISIBLE_BY(ITEMS, N)
    // Where ITEMS is a collection of integers and N 
    // is an integer factor.
    RESULT = new Container()
    ITEMS.resetNext()
    loop while ITEMS.hasNext()
        ITEM = ITEMS.getNext()
        if ITEM div N = 0 then
            RESULT.addItem(ITEM)
        end if
    end loop
    return RESULT
end function
```

### Literal Python translation:

```python
from ibdp_classes import Collection

def items_divisible_by(items: Collection[int], n: int) -> Collection[int]:
    result = Collection[int]()
    items.resetNext()
    while items.hasNext():
        item = items.getNext()
        if item % n == 0:
            result.addItem(item)
    return result
```

## `Stack`

A basic collection class that only supports methods `push`, `pop` and `isEmpty`.

### Example IB pseudocode:

```text
function PARENTHESIS_ERROR(ITEMS)
    // Where items is a collection of string characters.
    STACK = new Stack()
    RESULT = false
    ITEMS.resetNext()
    loop while ITEMS.hasNext()
        ITEM = ITEMS.getNext()
        if ITEM = "(" then
            STACK.push(ITEM)
        else if ITEM = ")" then
            if STACK.isEmpty() then
                RESULT = true
            else
                STACK.pop()
            end if
        end if
    end loop
    if not STACK.isEmpty() then
        RESULT = true
    end if
    return RESULT
end function
```

### Literal Python translation:

```python
from ibdp_classes import Collection, Stack

def parenthesis_error(items: Collection[str]) -> bool:
    stack = Stack[str]()
    result = False
    items.resetNext()
    while items.hasNext():
        item = items.getNext()
        if item == "(":
            stack.push(item)
        elif item == ")":
            if stack.isEmpty():
                result = True
            else:
                stack.pop()
    if not stack.isEmpty():
        result = True
    return result
```

## `Queue`

A basic collection class that only supports methods `enqueue`, `dequeue` and `isEmpty`.

### Example IB pseudocode:

```text
function KEEP_RESPECTIVE_LEAST(A, B)
    // Where A and B are collections containing integers.
    A.resetNext()
    B.resetNext()
    QUEUE = new Queue()
    loop while A.hasNext() or B.hasNext()
        if not A.hasNext() then
            QUEUE.enqueue(B.getNext())
        else if not B.hasNext() then
            QUEUE.enqueue(A.getNext())
        else
            ITEM_A = A.getNext()
            ITEM_B = B.getNext()
            if ITEM_A < ITEM_B then
                QUEUE.enqueue(ITEM_A)
            else
                QUEUE.enqueue(ITEM_B)
            end if
        end if
    end loop
    return QUEUE
end function
```

### Literal Python translation:

```python
from ibdp_classes import Collection, Queue

def keep_respective_least(a: Collection[int], b: Collection[int]) -> Queue[int]:
    a.resetNext()
    b.resetNext()
    queue = Queue[int]()
    while a.hasNext() or b.hasNext():
        if not a.hasNext():
            queue.enqueue(b.getNext())
        elif not b.hasNext():
            queue.enqueue(a.getNext())
        else:
            item_a = a.getNext()
            item_b = b.getNext()
            if item_a < item_b:
                queue.enqueue(item_a)
            else:
                queue.enqueue(item_b)
    return queue
```

