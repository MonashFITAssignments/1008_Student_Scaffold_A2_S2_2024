""" Hash Table ADT

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor & Rupert Ebeling'
__docformat__ = 'reStructuredText'
__modified__ = '15/08/2023'
__since__ = '31/03/2023'

from data_structures.referential_array import ArrayR
from data_structures.linked_list import LinkedList
from typing import TypeVar, Generic

T = TypeVar('T')


class HashTableSeparateChaining(Generic[T]):
    """
    Separate Chaining Hash Table

    constants:
        MIN_CAPACITY: smallest valid table size
        DEFAULT_TABLE_SIZE: default table size used in the __init__
        DEFAULT_HASH_TABLE: default hash base used for the hash function

    attributes:
        count: number of elements in the hash table
        array: used to represent our internal array
    """
    MIN_CAPACITY = 1

    DEFAULT_TABLE_SIZE = 17
    DEFAULT_HASH_BASE = 31

    def __init__(self, table_size: int = DEFAULT_TABLE_SIZE) -> None:
        """
        :complexity: O(A) where A is complexity of ArrayR.__init__()
        """
        self.count = 0
        self.table = ArrayR(max(self.MIN_CAPACITY, table_size))

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table
        :complexity: O(1)
        """
        return self.count

    def __delitem__(self, key: str) -> None:
        """
        Deletes an item from our hash table
        :raises KeyError: when the key doesn't exist
        """
        position = self.hash(key)
        if self.table[position] is None:
            raise KeyError(key)

        for index, item in enumerate(self.table[position]):
            if item[0] == key:
                if len(self.table[position]) <= 1:
                    self.table[position] = None
                else:
                    self.table[position].delete_at_index(index)

                self.count -= 1
                return

        raise KeyError(key)

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set a (key, data) pair in our hash table
        """
        position = self.hash(key)
        if self.table[position] is None:
            self.table[position] = LinkedList()

        # Attempt to find the key in our linked list
        if len(self.table[position]) > 0:
            for index, item in enumerate(self.table[position]):
                if item[0] == key:
                    # If found update the data
                    self.table[position][index] = (key, data)
                    return
                
        # self.table[position].insert(0, (key, data)) # To insert at the beginning 
        self.table[position].append((key, data))
        self.count += 1

    def __getitem__(self, key: str) -> T:
        """
        Get the data associated with a key
        :raises KeyError: when the key doesn't exist
        """
        position = self.hash(key)
        if self.table[position] is None:
            raise KeyError(key)
        for item in self.table[position]:
            if item[0] == key:
                return item[1]

        raise KeyError(key)

    def is_empty(self):
        """
        Returns whether the hash table is empty
        :complexity: O(1)
        """
        return self.count == 0

    def hash(self, key: str) -> int:
        """
        Universal Hash function
        :post: returns a valid position (0 <= value < table_size)
        :complexity: O(K) where K is the size of the key
        """
        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % len(self.table)
            a = a * HashTableSeparateChaining.DEFAULT_HASH_BASE % (len(self.table) - 1)
        return value

    def insert(self, key: str, data: T) -> None:
        """
        Utility method to call our setitem method
        :see: #__setitem__(self, key: str, data: T)
        """
        self[key] = data

    def __iter__(self):
        """
        Returns an iterator for the hash table
        :complexity: O(N) where N number of items in our hash table
        """
        for list in self.table:
            if list is not None:
                for item in list:
                    yield item[1]

    def keys(self) -> ArrayR[str]:
        """
        Returns all keys in the hash table
        :complexity: O(N) where N number of items in our hash table
        """
        res = ArrayR(self.count)
        i = 0
        for list in self.table:
            if list is not None:
                for item in list:
                    res[i] = item[0]
                    i += 1
        return res

    def values(self) -> ArrayR[T]:
        """
        Returns all values in the hash table
        :complexity: O(N) where N number of items in our hash table
        """
        res = ArrayR(self.count)
        i = 0
        for list in self.table:
            if list is not None:
                for item in list:
                    res[i] = item[1]
                    i += 1
        return res

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order)
        :complexity: O(N) where N number of items in our hash table
        """
        result = ""
        for list in self.table:
            if list is not None:
                first = True
                for item in list:
                    if not first:
                        result += ' -> '
                    (key, value) = item
                    result += "(" + str(key) + "," + str(value) + ")"
                    first = False
                result += '\n'
        return result
    
    def __repr__(self) -> str:
        return str(self)
