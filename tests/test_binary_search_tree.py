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

    bst.add(29, "Denis")
    bst.add(35, "Dima")
    bst.add(28, "Egor")

    assert bst.is_empty() is False
    assert len(bst) == 3


def test_add_node3():
    bst = BinaryTree()

    bst.add(29, "Denis")
    bst.add(35, "Dima")
    bst.add(28, "Egor")
    bst.add(28, "E")

    assert bst.is_empty() is False
    assert len(bst) == 3


def test_find_value1():
    bst = BinaryTree()

    result = bst.find("Key")
    assert result is None


def test_find_value2():
    bst = BinaryTree()

    bst.add(10, "Denis")

    result = bst.find(10)
    assert result == "Denis"


def test_find_value3():
    bst = BinaryTree()

    bst.add(10, "Denis")
    bst.add(11, "Dima")
    bst.add(9, "Egor")

    result = bst.find(11)
    assert result == "Dima"


def test_find_value4():
    bst = BinaryTree()

    bst.add(10, "Denis")
    bst.add(11, "Dima")
    bst.add(9, "Egor")

    result = bst.find(9)
    assert result == "Egor"


def test_find_value5():
    bst = BinaryTree()

    bst.add(10, "Denis")
    bst.add(11, "Dima")
    bst.add(9, "Egor")

    result = bst.find(11)
    assert result == "Dima"


def test_find_value6():
    bst = BinaryTree()

    bst.add(10, "Denis")
    bst.add(11, "Dima")
    bst.add(9, "Egor")

    result = bst.find(13)
    assert result is None
