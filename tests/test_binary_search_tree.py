'''Tests of binary search tree.'''

import pytest

from binary_search_tree.binary_serch_tree import BinaryTree
from binary_search_tree.node import Node


def test_make_node():
    node = Node(10, 'Test')

    assert str(node) == 'key: 10 value: Test'


def test_make_bst():
    bst = BinaryTree()

    assert bst.is_empty() is True
    assert len(bst) == 0


def test_add_node1():
    bst = BinaryTree()

    bst.add(10, 'Denis')

    assert bst.is_empty() is False
    assert len(bst) == 1


def test_add_node2():
    bst = BinaryTree()

    bst.add(29, 'Denis')
    bst.add(35, 'Dima')
    bst.add(28, 'Egor')

    assert bst.is_empty() is False
    assert len(bst) == 3


def test_add_node3():
    bst = BinaryTree()

    bst.add(29, 'Denis')
    bst.add(35, 'Dima')
    bst.add(28, 'Egor')
    bst.add(28, 'E')

    assert bst.is_empty() is False
    assert len(bst) == 3


def test_find_value1():
    bst = BinaryTree()

    result1 = bst.find('Key')
    result2 = bst['key']

    assert result1 is None
    assert result2 is None
    assert ('key' in bst) is False


def test_find_value2():
    bst = BinaryTree()

    bst.add(10, 'Denis')

    result1 = bst.find(10)
    result2 = bst.find(10)

    assert result1 == 'Denis'
    assert result2 == 'Denis'
    assert (10 in bst) is True


def test_find_value3():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(11, 'Dima')
    bst.add(9, 'Egor')

    result1 = bst.find(11)
    result2 = bst[11]

    assert result1 == 'Dima'
    assert result2 == 'Dima'
    assert (11 in bst) is True


def test_find_value4():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(11, 'Dima')
    bst.add(9, 'Egor')

    result1 = bst.find(9)
    result2 = bst[9]

    assert result1 == 'Egor'
    assert result2 == 'Egor'
    assert (9 in bst) is True


def test_find_value5():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(11, 'Dima')
    bst.add(9, 'Egor')

    result1 = bst.find(11)
    result2 = bst[11]

    assert result1 == 'Dima'
    assert result2 == 'Dima'
    assert (11 in bst) is True


def test_find_value6():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(11, 'Dima')
    bst.add(9, 'Egor')

    result1 = bst.find(13)
    result2 = bst[13]

    assert result1 is None
    assert result2 is None
    assert (13 in bst) is False


def test_min1():
    bst = BinaryTree()

    assert bst.min() is None


def test_min2():
    bst = BinaryTree()

    bst.add(10, 'Denis')

    assert bst.min() == 10


def test_min3():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(9, 'Dima')

    assert bst.min() == 9


def test_min4():
    bst = BinaryTree()

    bst.add(10, 'Denis')
    bst.add(9, 'Dima')
    bst.add(11, 'Egor')

    assert bst.min() == 9
