import unittest
from data_structures.merge_sort import merge_sort, merge


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [5]
        self.sorted = [1, 2, 3, 10]
        self.unsorted = [8, 1, 94, 43, 33]

    def testEmpty(self):
        expected = []
        actual = merge_sort(self.empty)
        self.assertEqual(expected, actual)

    def testSingle(self):
        expected = [5]
        actual = merge_sort(self.single)
        self.assertEqual(expected, actual)

    def testSorted(self):
        expected = [1, 2, 3, 10]
        actual = merge_sort(self.sorted)
        self.assertEqual(expected, actual)

    def testUnsorted(self):
        expected = [1, 8, 33, 43, 94]
        actual = merge_sort(self.unsorted)
        self.assertEqual(expected, actual)


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [5]
        self.sorted1 = [1, 2, 3, 4]
        self.sorted2 = [4, 7, 9, 10]
        self.sorted3 = [5, 6, 7, 8]

    def testTwoEmpty(self):
        expected = []
        actual = merge(self.empty, self.empty)
        self.assertEqual(expected, actual)

    def testLeftEmpty(self):
        expected = [5]
        actual = merge(self.empty, self.single)
        self.assertEqual(expected, actual)

    def testRightEmpty(self):
        expected = [5]
        actual = merge(self.single, self.empty)
        self.assertEqual(expected, actual)

    def testTwoOnes(self):
        expected = [5, 5]
        actual = merge(self.single, self.single)
        self.assertEqual(expected, actual)

    def testTwoNonOverlap(self):
        expected = [1, 2, 3, 4, 4, 7, 9, 10]
        actual = merge(self.sorted1, self.sorted2)
        self.assertEqual(expected, actual)

    def testTwoOverlap(self):
        expected = [4, 5, 6, 7, 7, 8, 9, 10]
        actual = merge(self.sorted2, self.sorted3)
        self.assertEqual(expected, actual)

    def testBackwards(self):
        expected = [1, 2, 3, 4, 4, 7, 9, 10]
        actual = merge(self.sorted2, self.sorted1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
