import unittest
from data_structures.radix_sort import radix_sort


class TestInsertSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [532]
        self.sorted = [45, 123, 225, 999]
        self.unsorted = [372, 223, 98, 111, 999]

    def testEmpty(self):
        expected = []
        actual = radix_sort(self.empty)
        self.assertEqual(expected, actual)

    def testSingle(self):
        expected = [532]
        actual = radix_sort(self.single)
        self.assertEqual(expected, actual)

    def testSorted(self):
        expected = [45, 123, 225, 999]
        actual = radix_sort(self.sorted)
        self.assertEqual(expected, actual)

    def testUnsorted(self):
        expected = [98, 111, 223, 372, 999]
        actual = radix_sort(self.unsorted)
        self.assertEqual(expected, actual)

    def testBaseTwo(self):
        unsorted = [0b110, 0b101, 0b1111111, 0b1, 0b0]
        expected = [0b0, 0b1, 0b101, 0b110, 0b1111111]
        actual = radix_sort(unsorted, 2)
        self.assertEqual(expected, actual)

    def testHexadecimal(self):
        unsorted = [0xff, 0x1, 0x2b8c, 0x0, 0xfffff]
        expected = [0x0, 0x1, 0xff, 0x2b8c, 0xfffff]
        actual = radix_sort(unsorted, 16)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
