
from typing import TypeVar

from data_structures.node import Node
from data_structures.queue_adt import Queue

T = TypeVar("T")
__author__ = "Rupert Ebeling"


class LinkedQueue(Queue[T]):
    """ Linked Queue.

    Attributes:
         front: the element at the front of the queue.
         rear: the element at the rear of the queue.
    """
    MIN_CAPACITY = 0

    def __init__(self) -> None:
        Queue.__init__(self)
        self.front = None
        self.rear = None

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :raises Exception: if the queueu is full
        """
        # Case 1: Empty queue
        if self.front is None:
            self.front = Node(item)
            self.rear = self.front
            self.length += 1
            return

        # Case 2: Non Empty queue
        # Add to the rear
        new_node = Node(item)
        self.rear.link = new_node
        self.rear = new_node
        self.length += 1

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        # Case 1: Single element in the queue
        if self.front == self.rear:
            item = self.front.item
            self.front = None
            self.rear = None
            self.length -= 1
            return item

        # Case 2: Multiple elements in the queue
        item = self.front.item
        self.front = self.front.link
        self.length -= 1
        return item

    def peek(self) -> T:
        """ Returns the element at the queue's front without deleting it.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.item

    def peek_node(self) -> Node:
        """ Returns the node at the queue's front without deleting it.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front

    def is_full(self) -> bool:
        """ Checks if the queue is full.
        Unlike an array-based queue, a linked queue cannot be full, unless
        the system runs out of memory which is a different issue.
        """
        return False

    def clear(self) -> None:
        """ Clears all elements from the queue. """
        Queue.__init__(self)
        self.front = None
        self.rear = None

    def __str__(self) -> str:
        """ Returns a string representation of the queue."""
        i = self.front
        result = ""
        count = 1  # 1-based counting
        while i is not None:
            result += f"p{count}: " + (str(i.item) if type(i.item) != str else "'{0}'".format(i.item))
            if i.link is not None:
                result += ", "
            i = i.link
            count += 1
        return result

    def __repr__(self) -> str:
        """Returns a string representation of the queue object.
        Useful for debugging or when the queue is held in another data structure."""
        return str(self)


def test_linked_queue() -> None:
    p1 = "person 1"
    p2 = "person 2"
    p3 = "person 3"

    sample_lq = LinkedQueue()
    assert sample_lq.is_empty()
    assert not sample_lq.is_full()
    assert len(sample_lq) == 0
    sample_lq.append(p1)

    assert not sample_lq.is_empty()
    assert sample_lq.peek() == p1
    assert len(sample_lq) == 1
    assert sample_lq.peek_node().item == p1
    assert sample_lq.peek_node().link is None

    sample_lq.append(p2)
    assert sample_lq.peek() == p1
    assert len(sample_lq) == 2

    sample_lq.append(p3)
    assert sample_lq.peek() == p1
    assert len(sample_lq) == 3
    print(sample_lq)
    assert sample_lq.serve() == p1
    assert sample_lq.peek() == p2
    assert len(sample_lq) == 2
    assert sample_lq.serve() == p2
    assert sample_lq.serve() == p3
    assert sample_lq.is_empty()
    assert len(sample_lq) == 0

    sample_lq.append(p1)
    sample_lq.clear()
    assert sample_lq.is_empty()
    assert len(sample_lq) == 0
    assert sample_lq.is_full() == False
    print("All tests pass.")


if __name__ == "__main__":
    test_linked_queue()
