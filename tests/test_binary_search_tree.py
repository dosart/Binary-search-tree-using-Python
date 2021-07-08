"""Tests of binary search tree."""

import pytest

from binary_search_tree.binary_serch_tree import BinaryTree
from binary_search_tree.node import Node


def test_make_node():
    node = Node(10, "Test")

    assert str(node) == "key: 10 value: Test"


def test_make_bst():
    bst = BinaryTree()

    assert bst.is_empty() is True
    assert len(bst) == 0


def test_add_node1():
    bst = BinaryTree()

    bst.add(10, "Denis")

    assert bst.is_empty() is False
    assert len(bst) == 1


def test_add_node2():
    bst = BinaryTree()

    bst.add(29, 'Denis')
    bst.add(35, 'Dima')
    bst.add(28, 'Egor')

    assert bst.is_empty() is False
    assert len(bst) == 3
