# -*- coding:utf-8 -*-

"""Node implementation for binary search tree."""


class Node(object):
    """Class implements node for binary search tree."""

    def __init__(self, key, value):
        """Class implements node for binary search tree.

        Args:
            key: _key for node
            value: _value for node
        """
        self._key = key
        self._value = value

        # pointers for left and right children
        self.left = None
        self.right = None

    def __str__(self):
        """Return a string representation of node.

        Returns:
            str(string): _key and _value
        """
        return "key: {0} value: {1}".join(self._key, self._value)
