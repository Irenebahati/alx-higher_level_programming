#!/usr/bin/python3
"""Defines  class LockedClass"""

class LockedClass:
    """
    Prevents the user from dynamically creating new instance attribute
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of locked class"""

        self.first_name = "first_name"
