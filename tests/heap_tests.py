import unittest
from data_structures.heap import Heap


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.h = Heap()

    def test_empty(self):
        self.h.insert(5, 'Five')
        self.assertEqual(self.h[0].val, 'Five')

    def test_left(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.assertEqual(self.h[1].val, 'Eight')

    def test_right(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.assertEqual(self.h[2].val, 'Ten')

    def test_new_min(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(3, 'Three')
        self.assertEqual(self.h[0].val, 'Three')
        self.assertEqual(self.h[1].val, 'Five')
        self.assertEqual(self.h[2].val, 'Ten')
        self.assertequal(self.h[3].val, 'Eight')

    def test_dupe(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(5, 'Five')
        self.assertEqual(self.h[0].val, 'Five')
        self.assertEqual(self.h[1].val, 'Eight')
        self.assertEqual(self.h[2].val, 'Five')

    def test_middle(self):
        self.h.insert(3, 'Three')
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(13, 'Thirteen')
        self.h.insert(11, 'Eleven')
        self.h.insert(12, 'Twelve')
        self.h.insert(4, 'Four')
        self.assertEqual(self.h[0].val, 'Three')
        self.assertEqual(self.h[1].val, 'Four')
        self.assertEqual(self.h[3].val, 'Five')


class TestUpheap(unittest.TestCase):
    pass


class TestDeleteMin(unittest.TestCase):
    def setUp(self):
        self.h = Heap()
        self.h.insert(5, 'Five')

    def test_one_and_empty(self):
        self.assertEqual(self.h.delete_min().val, 'Five')
        self.assertIsNone(self.h.delete_min())

    def test_left(self):
        self.h.insert(8, 'Eight')
        self.assertEqual(self.h.delete_min().val, 'Five')
        self.assertEqual(self.h[0].val, 'Eight')

    def test_right(self):
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.assertEqual(self.h.delete_min().val, 'Five')
        self.assertEqual(self.h[0].val, 'Eight')
        self.assertEqual(self.h[1].val, 'Ten')

    def test_dupe(self):
        self.h.insert(5, 'Five')
        self.assertEqual(self.h.delete_min().val, 'Five')
        self.assertEqual(self.h[0].val, 'Five')

    def test_new_min(self):
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(3, 'Three')
        self.assertEqual(self.h.delete_min().val, 'Three')
        self.assertEqual(self.h[0].val, 'Five')

    def test_multiple(self):
        self.h.insert(3, 'Three')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(13, 'Thirteen')
        self.h.insert(11, 'Eleven')
        self.h.insert(12, 'Twelve')
        self.h.insert(4, 'Four')
        self.assertEqual(self.h.delete_min().val, 'Three')
        self.assertEqual(self.h.delete_min().val, 'Four')
        self.assertEqual(self.h.delete_min().val, 'Five')
        self.assertEqual(self.h.delete_min().val, 'Eight')
        self.assertEqual(self.h.delete_min().val, 'Ten')


class TestDownheap(unittest.TestCase):
    pass
