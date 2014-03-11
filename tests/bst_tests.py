import unittest
from data_structures.bst import BSTree


class testInsert(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        self.assertEqual(self.bst.val, None)
        self.bst.insert(2)
        self.assertEqual(self.bst.val, 2)

    def testOne(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.left.val, None)
        self.assertEqual(self.bst.right.val, None)
        self.bst.insert(5)
        self.assertEqual(self.bst.left.val, None)
        self.assertEqual(self.bst.right.val, 5)

    def testFull(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.right.left.left.val, None)
        self.assertEqual(self.bst.right.left.right.val, None)
        self.bst.insert(4)
        self.assertEqual(self.bst.right.left.left.val, None)
        self.assertEqual(self.bst.right.left.right.val, 4)

    def testFullRepeat(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.right.left.left.val, None)
        self.assertEqual(self.bst.right.left.right.val, None)
        self.bst.insert(3)
        self.assertEqual(self.bst.right.left.left.val, None)
        self.assertEqual(self.bst.right.left.right.val, None)


class testContains(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        self.assertFalse(self.bst.contains(4))

    def testOne(self):
        self.bst.insert(2)
        self.assertTrue(self.bst.contains(2))
        self.assertFalse(self.bst.contains(4))

    def testFull(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertTrue(self.bst.contains(3))
        self.assertFalse(self.bst.contains(4))


class testSize(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        self.assertEqual(self.bst.size(), 0)

    def testOne(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.size(), 1)

    def testFull(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.size(), 5)

    def testFullRepeat(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.size(), 5)
        self.bst.insert(3)
        self.assertEqual(self.bst.size(), 5)


class testDepth(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        self.assertEqual(self.bst.depth(), 0)

    def testOne(self):
        self.bst.insert(2)
        self.assertEqual(self.bst.depth(), 1)

    def testFull(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.depth(), 3)

    def testFullRepeat(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.depth(), 3)
        self.bst.insert(3)
        self.assertEqual(self.bst.depth(), 3)


class testBalance(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        self.assertEqual(self.bst.balance(), 0)

    def testOne(self):
        self.assertEqual(self.bst.balance(), 0)

    def testFullRight(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.balance(), -1)

    def testFullLeft(self):
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(3)
        self.assertEqual(self.bst.balance(), 2)

    def testFullEven(self):
        self.bst.insert(3)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(2)
        self.bst.insert(8)
        self.assertEqual(self.bst.balance(), 0)


if __name__ == '__main__':
    unittest.main()
