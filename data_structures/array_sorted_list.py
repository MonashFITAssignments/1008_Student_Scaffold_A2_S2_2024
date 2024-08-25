""" Array-based implementation of SortedList ADT. """

from data_structures.referential_array import ArrayR
from data_structures.abstract_sorted_list import SortedList, T

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'


class ArraySortedList(SortedList[T]):
    """ SortedList ADT implemented with arrays. """
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        """ ArraySortedList object initialiser. """

        # first, calling the basic initialiser
        SortedList.__init__(self)

        # initialising the internal array
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def reset(self):
        """ Reset the list. """
        SortedList.__init__(self)

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        if index < 0 or len(self) <= index:
            raise IndexError('Out of bounds access in array.')
        return self.array[index]

    def __contains__(self, item):
        """ Checks if item is in the list. """
        try:
            _ = self.index(item)
            return True
        except ValueError:
            return False

    def _shuffle_right(self, index: int) -> None:
        """ Shuffle items to the right up to a given position. """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def _shuffle_left(self, index: int) -> None:
        """ Shuffle items starting at a given position to the left. """
        for i in range(index, len(self)):
            self.array[i] = self.array[i + 1]

    def _resize(self) -> None:
        """ Resize the list. """
        # doubling the size of our list
        new_array = ArrayR(2 * len(self.array))

        # copying the contents
        for i in range(self.length):
            new_array[i] = self.array[i]

        # referring to the new array
        self.array = new_array

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        item = self[index]
        self.length -= 1
        self._shuffle_left(index)
        return item

    def index(self, item: T) -> int:
        """
            Find the position of a given item in the list,
            by means of calling the _index_to_add() method.
            Raise ValueError if the item is not found.
        """
        # try find the index
        index = self._index_to_add(item)

        if index < len(self) and self.array[index] == item:
            return index
        raise ValueError(f"{item} not found")

    def is_full(self):
        """ Check if the list is full. """
        return len(self) >= len(self.array)

    def add(self, item: T) -> None:
        """ Add new element to the list. """
        if self.is_full():
            self._resize()
        index = self._index_to_add(item)
        self._shuffle_right(index)
        self.array[index] = item
        self.length += 1

    def _index_to_add(self, item: T) -> int:
        """ Find the position where the new item should be placed.
        :complexity best: O(comp)   item is the middle element
        :complexity worst: O(logn * comp)  first or last element
                    comp - cost of comparision
                    n - length of the list
        """

        low = 0
        high = len(self) - 1

        # until we have checked all elements in the search space
        while low <= high:
            mid = (low + high) // 2
            # Found the item
            if self[mid] == item:
                return mid
            # check right of the remaining list
            elif self[mid] < item:
                low = mid + 1
            # check left of the remaining list
            else:
                high = mid - 1

        return low
