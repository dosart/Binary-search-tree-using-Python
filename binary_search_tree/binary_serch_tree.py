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

    def __getitem__(self, key):
        """Return value bu key.

        Args:
            key: key for find value

        Returns:
            value: value if key exist else None
        """
        return self.find(key)

    def __setitem__(self, key, value):
        """Add the given key and object to tree(iterative version).

        Args:
            key:  key for value
            value: value by key
        """
        self.add(key, value)

    def __contains__(self, key):
        """Return True if key contains in Tree.

        Args:
            key: key for search

        Returns:
            value: none if key not contains else value
        """
        return self.find(key) is not None

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

    def min(self):
        """Return min key(iterative version).

        Returns:
            key: min key in tree
        """
        if self.is_empty():
            return None

        cur = self._root
        while cur.left:
            cur = cur.left
        return cur

    def max(self):
        """Return max key(iterative version).

        Returns:
            key: max key in tree
        """
        if self.is_empty():
            return None

        cur = self._root
        while cur.right:
            cur = cur.right
        return cur

    def get_successor_key(self, key):
        """Return the node that contains next key.

        Args:
            key: key for search next key

        Returns:
            node: node contains next keys
        """
        successor = None
        cur = self._root
        while cur:
            if key < cur.key:
                successor = cur
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                if cur.right:
                    return self._min(cur.right)
                return successor
        return None

    def _add(self, key, value):
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
        cur = self._root
        while cur:
            if key > cur.key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                return cur.value
        return None

    def _min(self, root):
        parent = root
        while parent.left:
            parent = parent.left
        return parent
