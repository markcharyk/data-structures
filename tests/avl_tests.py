import unittest
from data_structures.avl_tree import Node, AVLTree


class TestInsert(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_empty(self):
        self.assertIsNone(self.tree.root)
        self.tree.insert(5)
        self.assertEqual(self.tree.root.val, 5)

    def test_one(self):
        self.tree.insert(2)
        self.assertIsNone(self.tree.root.left)
        self.assertIsNone(self.tree.root.right)
        self.tree.insert(5)
        self.assertEqual(self.tree.root.right.val, 5)

    def test_many(self):
        self.tree.insert(3)
        self.tree.insert(1)
        self.tree.insert(5)
        self.tree.insert(0)
        self.tree.insert(4)
        self.tree.insert(2)
        self.assertIsNone(self.tree.root.right.right)
        self.tree.insert(6)
        self.assertEqual(self.tree.root.right.right.val, 6)

    def test_balancing_insert(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(1)
        self.assertEqual(self.tree.root.val, 3)
        self.assertEqual(self.tree.root.left.val, 1)
        self.assertEqual(self.tree.root.right.val, 5)

    def test_non_root_balance_insert(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(8)
        self.tree.insert(6)
        self.tree.insert(7)
        self.assertEqual(self.tree.root.val, 5)
        self.assertEqual(self.tree.root.right.val, 7)
        self.assertEqual(self.tree.root.right.left.val, 6)
        self.assertEqual(self.tree.root.right.right.val, 8)


class TestHeight(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_empty(self):
        self.assertEqual(self.tree.height(self.tree.root), -1)

    def test_one(self):
        self.tree.insert(2)
        self.assertEqual(self.tree.height(self.tree.root), 0)

    def test_many(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(1)
        self.tree.insert(8)
        self.tree.insert(3)
        self.assertEqual(self.tree.height(self.tree.root), 2)


class TestRemove(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_empty(self):
        self.tree.remove(2)
        self.assertIsNone(self.tree.root)

    def test_one(self):
        self.tree.insert(2)
        self.tree.remove(2)
        self.assertIsNone(self.tree.root)

    def test_remove_leaf(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.tree.remove(6)
        self.assertIsNone(self.tree.root.right.left)
        self.assertEqual(self.tree.root.right.val, 7)
        self.assertEqual(self.tree.root.right.right.val, 8)

    def test_remove_mid(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.tree.remove(7)
        self.assertIsNone(self.tree.root.right.right)
        self.assertEqual(self.tree.root.right.val, 8)
        self.assertEqual(self.tree.root.right.left.val, 6)

    def test_remove_root(self):
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.insert(7)
        self.tree.insert(2)
        self.tree.insert(4)
        self.tree.insert(6)
        self.tree.insert(8)
        self.tree.remove(5)
        self.assertEqual(self.tree.root.val, 6)
        self.assertIsNone(self.tree.root.right.left)
        self.assertEqual(self.tree.root.right.val, 7)
        self.assertEqual(self.tree.root.right.right.val, 8)


class TestBalancing(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(6)
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)
        self.n7 = Node(7)
        self.n8 = Node(8)
        self.n9 = Node(9)

    def test_left(self):
        self.tree.root.right.right = self.n7
        self.n7.parent = self.tree.root.right
        self.tree.root.right.right.right = self.n8
        self.n8.parent = self.tree.root.right.right
        self.tree.rotate_left(self.tree.root.right)
        self.assertEqual(self.tree.root.right.val, 7)
        self.assertEqual(self.tree.root.right.left.val, 6)
        self.assertEqual(self.tree.root.right.right.val, 8)

    def test_right(self):
        self.tree.root.left.left = self.n3
        self.n3.parent = self.tree.root.left
        self.tree.root.left.left.left = self.n2
        self.n2.parent = self.tree.root.left.left
        self.tree.rotate_right(self.tree.root.left)
        self.assertEqual(self.tree.root.left.val, 3)
        self.assertEqual(self.tree.root.left.left.val, 2)
        self.assertEqual(self.tree.root.left.right.val, 4)


if __name__ == '__main__':
    unittest.main()
