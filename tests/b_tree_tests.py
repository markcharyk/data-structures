import unittest
from data_structures.b_tree import Node, BTree


class TestAddToNode(unittest.TestCase):
    def test_one(self):
        pass

    def test_two_overflow(self):
        pass


class TestDelFromNode(unittest.TestCase):
    def test_one_underflow(self):
        pass

    def test_two(self):
        pass


class TestIsInNode(unittest.TestCase):
    def test_first(self):
        pass

    def test_second(self):
        pass

    def not_there(self):
        pass


class TestSplitNode(unittest.TestCase):
    def test_split(self):
        pass


class TestSearchTree(unittest.TestCase):
    def test_at_root(self):
        pass

    def test_in_middle(self):
        pass

    def test_at_leaf(self):
        pass

    def test_not_in_tree(self):
        pass


class TestInsertTree(unittest.TestCase):
    def test_empty(self):
        pass

    def test_at_root(self):
        pass

    def test_no_split(self):
        pass

    def test_split_node(self):
        pass

    def test_new_level(self):
        pass


class TestDeleteTree(unittest.TestCase):
    def test_empty(self):
        pass

    def test_one_root(self):
        pass

    def test_two_root(self):
        pass

    def test_no_underflow(self):
        pass

    def test_underflow(self):
        pass

    def test_delete_level(self):
        pass
