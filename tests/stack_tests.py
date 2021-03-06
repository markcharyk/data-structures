import unittest
from data_structures.stack import Stack


class testPop(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def testEmptyList(self):
        self.assertRaises(IndexError, self.stack.pop)

    def testListOfOne(self):
        self.stack = Stack(1)
        self.assertEqual(self.stack.pop().val, 1)
        self.stack.push("Hello")
        self.assertEqual(self.stack.pop().val, "Hello")

    def testLongList(self):
        self.stack = Stack(10, 11, 12, 13, 14)
        self.assertEqual(self.stack.pop().val, 14)
        self.assertEqual(self.stack.pop().val, 13)

    def tearDown(self):
        self.stack = None


class testPush(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(10, 11, 12, 13, 14)

    def testEmpyList(self):
        self.stack = Stack()
        self.stack.push(10)
        self.assertEqual(self.stack.head.val, 10)

    def testListOfOne(self):
        self.stack = Stack()
        self.stack.push(10)
        self.stack.push(11)
        self.assertEqual(self.stack.head.val, 11)

    def testLongList(self):
        self.stack.push(15)
        self.assertEqual(self.stack.head.val, 15)

if __name__ == "__main__":
    unittest.main()
