"""Tests of binary search tree."""

import pytest

from binary_search_tree.binary_serch_tree import BinaryTree
from binary_search_tree.node import Node


def test_make_node():
    node = Node(10, 'Test')

    assert str(node) == 'key: 10 value: Test'


def test_make_bst():
    bst = BinaryTree()

    assert bst.is_empty() == True
    assert len(bst) == 0
