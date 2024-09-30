from enum import Enum


class Position(Enum):
    """
    This class represents the index of the head and tail of a list as 
    an enum to only allow the following indexes to be operated on.
    """
    HEAD = 0
    TAIL = -1