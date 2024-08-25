""" Implementation of a node in linked lists. """

from typing import TypeVar, Generic
T = TypeVar('T')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class Node(Generic[T]):
    """ Simple linked node. It contains an item and has a reference to next node. """

    def __init__(self, item: T = None) -> None:
        """ Node initialiser. """
        self.item = item
        self.link = None
