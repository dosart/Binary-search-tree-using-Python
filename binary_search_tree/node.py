# -*- coding:utf-8 -*-

"""Node implementation for binary search tree."""


class Node(object):
    """Class implements node for binary search tree."""

    def __init__(self, key, value):
        """Class implements node for binary search tree.

        Args:
            key: key for node
            value: value for node
        """
        self.key = key
        self.value = value

        # pointers for left and right children
        self.left = None
        self.right = None

    def __str__(self):
        return "key: {0} value: {1}".join(self.key, self.value)
