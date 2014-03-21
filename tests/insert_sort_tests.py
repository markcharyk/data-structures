import unittest
from data_structures.insert_sort import insertion_sort


class TestInsertSort(unittest.TestCase):
    def setUp(self):
        """Set up some lists to be sorted"""
        self.empty = []
        self.single = [5]
        self.sorted = [1, 2, 3, 10]
        self.unsorted = [8, 1, 94, 43, 33]

    def testEmpty(self):
        """Test an empty list"""
        expected = []
        actual = insertion_sort(self.empty)
        self.assertEqual(expected, actual)

    def testSingle(self):
        """Test a list of one item"""
        expected = [5]
        actual = insertion_sort(self.single)
        self.assertEqual(expected, actual)

    def testSorted(self):
        """Test an already sorted list"""
        expected = [1, 2, 3, 10]
        actual = insertion_sort(self.sorted)
        self.assertEqual(expected, actual)

    def testUnsorted(self):
        """Test an unsorted list"""
        expected = [1, 8, 33, 43, 94]
        actual = insertion_sort(self.unsorted)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
