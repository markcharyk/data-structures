import unittest
from data_structures.ll_stack import LLStack


class testPop(unittest.TestCase):
    def setUp(self):
        self.stack = LLStack()

    def testEmptyList(self):
        self.assertRaises(IndexError, self.stack.pop)

    def testListOfOne(self):
        self.stack = LLStack(1)
        self.assertEqual(self.stack.pop().val, 1)
        self.stack.push("Hello")
        self.assertEqual(self.stack.pop().val, "Hello")

    def testLongList(self):
        self.stack = LLStack(10, 11, 12, 13, 14)
        self.assertEqual(self.stack.pop().val, 14)
        self.assertEqual(self.stack.pop().val, 13)

    def tearDown(self):
        self.stack = None


class testPush(unittest.TestCase):
    def setUp(self):
        self.stack = LLStack(10, 11, 12, 13, 14)

    def testEmpyList(self):
        self.stack = LLStack()
        self.stack.push(10)
        self.assertEqual(self.stack.head.val, 10)

    def testListOfOne(self):
        self.stack = LLStack()
        self.stack.push(10)
        self.stack.push(11)
        self.assertEqual(self.stack.head.val, 11)

    def testLongList(self):
        self.stack.push(15)
        self.assertEqual(self.stack.head.val, 15)

if __name__ == "__main__":
    unittest.main()
