"""Tests of binary search tree."""

import pytest

from binary_search_tree.binary_serch_tree import BinaryTree


def test_make_bst():
    bst = BinaryTree()

    assert bst.is_empty() == True
    assert len(bst) == 0
