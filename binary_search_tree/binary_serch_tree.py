# -*- coding:utf-8 -*-

"""Binary search tree implementation using oop style. Can be used as a dictionary."""

from binary_search_tree.node import Node


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

    def add(self, key, value):
        """Add the given key and object to tree(iterative version).

        Args:
            key:  key for value
            value: value by key
        """
        if self.is_empty():
            self._root = Node(key, value)
            self._count += 1
        else:
            self._add(key, value)

    def find(self, key):
        """Return value by key.

        Args:
            key: key for find value

        Returns:
            value: value if key exist else None
        """
        if self.is_empty():
            return None
        else:
            return self._find(key)

    def _add(self, key, value):
        """Add the given key and object to tree(iterative version).

        Args:
            key:  key for value
            value: value by key
        """
        parent = self._root
        cur = self._root
        while cur:
            parent = cur
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return
        new_node = Node(key, value)
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        self._count += 1

    def _find(self, key):
        """Return value by key.

        Args:
            key: key for find value

        Returns:
            value: value if key exist else None
        """
        cur = self._root
        while cur:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.value
        return None
