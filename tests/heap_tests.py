import unittest
from data_structures.heap import Heap, Node


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.h = Heap()

    def test_empty(self):
        self.h.insert(5, 'Five')
        self.assertEqual(self.h.heap[0].val, 'Five')

    def test_left(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.assertEqual(self.h.heap[1].val, 'Eight')

    def test_right(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.assertEqual(self.h.heap[2].val, 'Ten')

    def test_new_min(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(3, 'Three')
        self.assertEqual(self.h.heap[0].val, 'Three')
        self.assertEqual(self.h.heap[1].val, 'Five')
        self.assertEqual(self.h.heap[2].val, 'Ten')
        self.assertEqual(self.h.heap[3].val, 'Eight')

    def test_dupe(self):
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(5, 'Five')
        self.assertEqual(self.h.heap[0].val, 'Five')
        self.assertEqual(self.h.heap[1].val, 'Eight')
        self.assertEqual(self.h.heap[2].val, 'Five')

    def test_middle(self):
        self.h.insert(3, 'Three')
        self.h.insert(5, 'Five')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(13, 'Thirteen')
        self.h.insert(11, 'Eleven')
        self.h.insert(12, 'Twelve')
        self.h.insert(4, 'Four')
        self.assertEqual(self.h.heap[0].val, 'Three')
        self.assertEqual(self.h.heap[1].val, 'Four')
        self.assertEqual(self.h.heap[3].val, 'Five')


class TestUpheap(unittest.TestCase):
    def setUp(self):
        self.h = Heap()
        self.h.insert(5, 'Five')

    def test_once_left(self):
        self.h.heap.append(Node(3, 'Three'))
        self.h._upheap(1)
        self.assertEqual(self.h.heap[0].val, 'Three')
        self.assertEqual(self.h.heap[1].val, 'Five')

    def test_once_right(self):
        self.h.insert(8, 'Eight')
        self.h.heap.append(Node(3, 'Three'))
        self.h._upheap(2)
        self.assertEqual(self.h.heap[0].val, 'Three')
        self.assertEqual(self.h.heap[2].val, 'Five')

    def test_many(self):
        self.h.insert(3, 'Three')
        self.h.insert(8, 'Eight')
        self.h.insert(10, 'Ten')
        self.h.insert(13, 'Thirteen')
        self.h.insert(11, 'Eleven')
        self.h.insert(12, 'Twelve')
        self.h.insert(4, 'Four')
        self.h.heap.append(Node(2, 'Two'))
        self.h._upheap(len(self.h.heap) - 1)
        self.assertEqual(self.h.heap[0].val, 'Two')


# class TestDeleteMin(unittest.TestCase):
#     def setUp(self):
#         self.h = Heap()
#         self.h.insert(5, 'Five')

#     def test_one_and_empty(self):
#         self.assertEqual(self.h.delete_min(), 'Five')
#         self.assertIsNone(self.h.delete_min())

#     def test_left(self):
#         self.h.insert(8, 'Eight')
#         self.assertEqual(self.h.delete_min(), 'Five')
#         self.assertEqual(self.h.heap[0].val, 'Eight')

#     def test_right(self):
#         self.h.insert(8, 'Eight')
#         self.h.insert(10, 'Ten')
#         self.assertEqual(self.h.delete_min(), 'Five')
#         self.assertEqual(self.h.heap[0].val, 'Eight')
#         self.assertEqual(self.h.heap[1].val, 'Ten')

#     def test_dupe(self):
#         self.h.insert(5, 'Five')
#         self.assertEqual(self.h.delete_min(), 'Five')
#         self.assertEqual(self.h.heap[0].val, 'Five')

#     def test_new_min(self):
#         self.h.insert(8, 'Eight')
#         self.h.insert(10, 'Ten')
#         self.h.insert(3, 'Three')
#         self.assertEqual(self.h.delete_min(), 'Three')
#         self.assertEqual(self.h.heap[0].val, 'Five')

#     def test_multiple(self):
#         self.h.insert(3, 'Three')
#         self.h.insert(8, 'Eight')
#         self.h.insert(10, 'Ten')
#         self.h.insert(13, 'Thirteen')
#         self.h.insert(11, 'Eleven')
#         self.h.insert(12, 'Twelve')
#         self.h.insert(4, 'Four')
#         self.assertEqual(self.h.delete_min(), 'Three')
#         self.assertEqual(self.h.delete_min(), 'Four')
#         self.assertEqual(self.h.delete_min(), 'Five')
#         self.assertEqual(self.h.delete_min(), 'Eight')
#         self.assertEqual(self.h.delete_min(), 'Ten')


# class TestDownheap(unittest.TestCase):
#     def setUp(self):
#         self.h = Heap()
#         self.h.insert(5, 'Five')

#     def test_once_left(self):
#         self.h.heap.append(Node(2, 'Two'))
#         self.h.heap.append(Node(3, 'Three'))
#         self.h._downheap(0)
#         self.assertEqual(self.h.heap[0].val, 'Two')
#         self.assertEqual(self.h.heap[1].val, 'Five')

#     def test_once_right(self):
#         self.h.heap.append(Node(2, 'Three'))
#         self.h.heap.append(Node(3, 'Two'))
#         self.h._downheap(0)
#         self.assertEqual(self.h.heap[0].val, 'Two')
#         self.assertEqual(self.h.heap[2].val, 'Five')

#     def test_many(self):
#         self.h.insert(3, 'Three')
#         self.h.insert(8, 'Eight')
#         self.h.insert(10, 'Ten')
#         self.h.insert(13, 'Thirteen')
#         self.h.insert(11, 'Eleven')
#         self.h.insert(12, 'Twelve')
#         self.h.insert(4, 'Four')
#         self.h.heap.append(Node(2, 'Two'))
#         self.h._downheap(0)
#         self.assertEqual(self.h.heap[0].val, 'Two')


if __name__ == '__main__':
    unittest.main()
