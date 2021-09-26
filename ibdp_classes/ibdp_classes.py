from typing import Generic, TypeVar

T = TypeVar("T")


class _Base(Generic[T]):
    def __init__(self, elements: list[T]) -> None:
        self._elements = elements.copy()

    def __str__(self) -> str:
        return f"{type(self).__name__}: {self._elements}"


class _KnowsIfEmpty(_Base[T]):
    def isEmpty(self) -> bool:
        """Returns whether the structure contains any elements."""
        return not self._elements


class Array(_Base[T]):
    """A basic array structure that only allows random access.

    Example:

    ```
    array = Array(["a", "b", "c"])
    array[0] = "d"
    print(array[0])
    ```
    """

    def __init__(self, elements: list[T]) -> None:
        super().__init__(elements)

    def __setitem__(self, index: int, value: T) -> None:
        if isinstance(index, int):
            if 0 <= index < len(self._elements):
                self._elements[index] = value

            raise Exception("Array index out of bounds.")
        raise Exception("Non integer Array index.")

    def __getitem__(self, index: int) -> T:
        if isinstance(index, int):
            if 0 <= index < len(self._elements):
                return self._elements[index]

            raise Exception("Array index out of bounds.")
        raise Exception("Non integer Array index.")


class Collection(_KnowsIfEmpty[T]):
    """A basic collection class that only supports methods `hasNext`,
    `getNext`, `resetNext`, `addItem` and `isEmpty`."""

    def __init__(self, elements: list[T] = []) -> None:
        super().__init__(elements)
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

    def __init__(self, elements: list[T] = []) -> None:
        super().__init__(elements)

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

    def __init__(self, elements: list[T] = []) -> None:
        super().__init__(elements)

    def enqueue(self, element: T) -> None:
        """Adds element `element` to the back of the queue."""
        self._elements.append(element)

    def dequeue(self) -> T:
        """Removes and returns the element at the front of the queue."""
        if self._elements:
            x, *self._elements = self._elements
            return x

        raise Exception("Attempted to dequeue an empty queue.")
