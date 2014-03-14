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


class testInOrder(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()
        self.actual = []

    def testEmpty(self):
        for i in self.bst.in_order():
            self.actual.append(i)
        self.assertEqual([], self.actual)

    def testOne(self):
        self.bst.insert(2)
        for i in self.bst.in_order():
            self.actual.append(i)
        self.assertEqual([2], self.actual)

    def testMany(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        for i in self.bst.in_order():
            self.actual.append(i)
        self.assertEqual([1, 2, 3, 5, 8], self.actual)


class testPreOrder(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()
        self.actual = []

    def testEmpty(self):
        for i in self.bst.pre_order():
            self.actual.append(i)
        self.assertEqual([], self.actual)

    def testOne(self):
        self.bst.insert(2)
        for i in self.bst.pre_order():
            self.actual.append(i)
        self.assertEqual([2], self.actual)

    def testMany(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        for i in self.bst.pre_order():
            self.actual.append(i)
        self.assertEqual([2, 1, 5, 3, 8], self.actual)


class testPostOrder(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()
        self.actual = []

    def testEmpty(self):
        for i in self.bst.post_order():
            self.actual.append(i)
        self.assertEqual([], self.actual)

    def testOne(self):
        self.bst.insert(2)
        for i in self.bst.post_order():
            self.actual.append(i)
        self.assertEqual([2], self.actual)

    def testMany(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        for i in self.bst.post_order():
            self.actual.append(i)
        self.assertEqual([1, 3, 8, 5, 2], self.actual)


class testBreadthFirst(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()
        self.actual = []

    def testEmpty(self):
        for i in self.bst.breadth_first():
            self.actual.append(i)
        self.assertEqual([], self.actual)

    def testOne(self):
        self.bst.insert(2)
        for i in self.bst.breadth_first():
            self.actual.append(i)
        self.assertEqual([2], self.actual)

    def testMany(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        for i in self.bst.breadth_first():
            self.actual.append(i)
        self.assertEqual([2, 1, 5, 3, 8, 4, 7], self.actual)


class testDelete(unittest.TestCase):
    def setUp(self):
        self.bst = BSTree()

    def testEmpty(self):
        exp_bst = self.bst
        self.bst.delete(2)
        self.assertEqual(exp_bst, self.bst)

    def testOne(self):
        exp_bst = self.bst
        self.bst.insert(2)
        self.bst.delete(2)
        self.assertEqual(exp_bst, self.bst)

    def testManyDeleteNoLeaves(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.delete(7)
        expected = [2, 1, 5, 3, 8, 4]
        actual = []
        for i in self.bst.breadth_first():
            actual.append(i)
        self.assertEqual(expected, actual)

    def testManyDeleteOneLeaf(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.delete(3)
        expected = [2, 1, 5, 4, 8, 7]
        actual = []
        for i in self.bst.breadth_first():
            actual.append(i)
        self.assertEqual(expected, actual)

    def testManyDeleteTwoLeaves(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.delete(5)
        expected = [2, 1, 4, 3, 8, 7]
        actual = []
        for i in self.bst.breadth_first():
            actual.append(i)
        self.assertEqual(expected, actual)

    def testManyDeleteRoot(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.delete(2)
        expected = [3, 1, 5, 4, 8, 7]
        actual = []
        for i in self.bst.breadth_first():
            actual.append(i)
        self.assertEqual(expected, actual)

    def testManyDeleteNone(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        expected = self.bst
        self.bst.delete(6)
        actual = self.bst
        self.assertEqual(expected, actual)

    def testFullTreeOnSingleNode(self):
        self.bst.insert(2)
        self.bst.insert(5)
        self.bst.insert(1)
        self.bst.insert(8)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.insert(4)
        self.bst.insert(3.5)
        self.bst.insert(4.5)
        expected = [2, 1, 5, 4, 8, 3.5, 4.5, 7]
        self.bst.delete(3)
        actual = []
        for i in self.bst.breadth_first():
            actual.append(i)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
