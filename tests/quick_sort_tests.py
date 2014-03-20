import unittest
from data_structures.quick_sort import quick_sort, select_pivot


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [5]
        self.sorted = [1, 2, 3, 10]
        self.unsorted = [8, 1, 94, 43, 33]
        self.expected = [1, 8, 33, 43, 94]

    def testEmpty(self):
        expected = []
        actual = quick_sort(self.empty)
        self.assertEqual(expected, actual)

    def testSingle(self):
        expected = [5]
        actual = quick_sort(self.single)
        self.assertEqual(expected, actual)

    def testSorted(self):
        expected = [1, 2, 3, 10]
        actual = quick_sort(self.sorted)
        self.assertEqual(expected, actual)

    def testUnsorted(self):
        actual = quick_sort(self.unsorted)
        self.assertEqual(self.expected, actual)

    def testRandom(self):
        actual = quick_sort(self.unsorted, 'random')
        self.assertEqual(self.expected, actual)

    def testMiddle(self):
        actual = quick_sort(self.unsorted, 'middle')
        self.assertEqual(self.expected, actual)

    def testMedian(self):
        actual = quick_sort(self.unsorted, 'median')
        self.assertEqual(self.expected, actual)

    def testIndex(self):
        actual = quick_sort(self.unsorted, -1)
        self.assertEqual(self.expected, actual)

    def testOutOfIndex(self):
        actual = quick_sort(self.unsorted, 10)
        self.assertEqual(self.expected, actual)


class TestPivotSelect(unittest.TestCase):
    def setUp(self):
        self.inp = [7, 2, 88, 4, 64]

    def testNone(self):
        self.assertEqual(7, select_pivot(self.inp, None))

    def testMiddle(self):
        self.assertEqual(88, select_pivot(self.inp, 'middle'))

    def testMedian(self):
        self.assertEqual(64, select_pivot(self.inp, 'median'))

    def testMedianTwo(self):
        inp = [5, 8]
        self.assertEqual(8, select_pivot(inp, 'median'))

    def testIndex(self):
        self.assertEqual(4, select_pivot(self.inp, 3))

    def testOutOfIndex(self):
        self.assertEqual(7, select_pivot(self.inp, 8))


if __name__ == '__main__':
    unittest.main()
