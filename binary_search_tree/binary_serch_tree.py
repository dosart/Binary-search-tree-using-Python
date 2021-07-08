# -*- coding:utf-8 -*-

"""Binary search tree implementation using oop style. Can be used as a dictionary."""


class BinaryTree(object):
    """Class implements dictionary using binary search tree."""

    def __init__(self):
        """Class implements dictionary using binary search tree."""
        self._root = None
        self._count = 0

    def __len__(self):
        """Return size of list.

        Returns:
            size(int): size of nodes
        """
        return self._count

    def is_empty(self):
        """Return True if tree is empty.

        Returns:
            bool: True if tree is empty else False
        """
        return self._count == 0
