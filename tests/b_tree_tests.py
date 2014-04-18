import unittest
from data_structures.b_tree import Node, BTree


class TestAddToNode(unittest.TestCase):
    def setUp(self):
        self.n = Node()

    def test_empty(self):
        self.n.add_to_node(4, 'Four')
        self.assertEqual(self.n.elems[0][1], 'Four')
        self.assertIsNone(self.n.elems[1][1])
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 1)

    def test_one_post(self):
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(5, 'Five')
        self.assertEqual(self.n.elems[0][1], 'Four')
        self.assertEqual(self.n.elems[1][1], 'Five')
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 2)

    def test_one_pre(self):
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(3, 'Three')
        self.assertEqual(self.n.elems[0][1], 'Three')
        self.assertEqual(self.n.elems[1][1], 'Four')
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 2)

    def test_two_post(self):
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(5, 'Five')
        self.n.add_to_node(6, 'Six')
        self.assertEqual(self.n.elems[0][1], 'Four')
        self.assertEqual(self.n.elems[1][1], 'Five')
        self.assertEqual(self.n.elems[2][1], 'Six')
        self.assertEqual(self.n.count, 3)

    def test_two_mid(self):
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(6, 'Six')
        self.n.add_to_node(5, 'Five')
        self.assertEqual(self.n.elems[0][1], 'Four')
        self.assertEqual(self.n.elems[1][1], 'Five')
        self.assertEqual(self.n.elems[2][1], 'Six')
        self.assertEqual(self.n.count, 3)

    def test_two_pre(self):
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(5, 'Five')
        self.n.add_to_node(3, 'Three')
        self.assertEqual(self.n.elems[0][1], 'Three')
        self.assertEqual(self.n.elems[1][1], 'Four')
        self.assertEqual(self.n.elems[2][1], 'Five')
        self.assertEqual(self.n.count, 3)


class TestDelFromNode(unittest.TestCase):
    def setUp(self):
        self.n = Node()
        self.n.add_to_node(4, 'Four')

    def test_one_underflow(self):
        self.n.del_from_node(0)
        self.assertIsNone(self.n.elems[0][1])
        self.assertIsNone(self.n.elems[1][1])
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 0)

    def test_two_pre(self):
        self.n.add_to_node(5, 'Five')
        self.n.del_from_node(0)
        self.assertEqual(self.n.elems[0][1], 'Five')
        self.assertIsNone(self.n.elems[1][1])
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 1)

    def test_two_post(self):
        self.n.add_to_node(5, 'Five')
        self.n.del_from_node(1)
        self.assertEqual(self.n.elems[0][1], 'Four')
        self.assertIsNone(self.n.elems[1][1])
        self.assertIsNone(self.n.elems[2][1])
        self.assertEqual(self.n.count, 1)


class TestHas(unittest.TestCase):
    def setUp(self):
        self.n = Node()

    def test_empy(self):
        self.assertFalse(self.n.has(4))

    def test_first(self):
        self.n.add_to_node(4, 'Four')
        self.assertTrue(self.n.has(4))

    def test_second(self):
        self.n.add_to_node(3, 'Three')
        self.n.add_to_node(4, 'Four')
        self.assertTrue(self.n.has(4))

    def not_there(self):
        self.n.add_to_node(3, 'Three')
        self.n.add_to_node(4, 'Four')
        self.assertFalse(self.n.has(5))


class TestSplitNode(unittest.TestCase):
    def setUp(self):
        self.n = Node()
        self.n.add_to_node(4, 'Four')
        self.n.add_to_node(5, 'Five')
        self.n.add_to_node(6, 'Six')

    def test_split(self):
        a, b, c = self.n.split_node()
        self.assertEqual(a.elems[0][0], 4)
        self.assertEqual(a.elems[0][1], 'Four')
        self.assertIsNone(a.elems[1][1])
        self.assertEqual(a.count, 1)
        self.assertEqual(c.elems[0][0], 6)
        self.assertEqual(c.elems[0][1], 'Six')
        self.assertIsNone(c.elems[1][1])
        self.assertEqual(c.count, 1)
        self.assertEqual(b, (5, 'Five'))


class TestSearchTree(unittest.TestCase):
    def setUp(self):
        four = Node(4, 'Four')
        two = Node(2, 'Two')
        two.parent = four
        six_eight = Node(6, 'Six')
        six_eight.add_to_node(8, 'Eight')
        six_eight.parent = four
        four.left = two
        four.right = six_eight
        one = Node(1, 'One')
        one.parent = two
        three = Node(3, 'Three')
        three.parent = two
        two.left = one
        two.right = three
        five = Node(5, 'Five')
        five.parent = six_eight
        seven = Node(7, 'Seven')
        seven.parent = six_eight
        nine = Node(9, 'Nine')
        nine.parent = six_eight
        six_eight.left = five
        six_eight.mid = seven
        six_eight.right = nine
        self.b = BTree()
        self.b.root = four

    def test_at_root(self):
        self.assertEqual(self.b.search(4), 'Four')

    def test_in_middle(self):
        self.assertEqual(self.b.search(2), 'Two')
        self.assertEqual(self.b.search(8), 'Eight')

    def test_at_leaf(self):
        self.assertEqual(self.b.search(1), 'One')
        self.assertEqual(self.b.search(9), 'Nine')

    def test_not_in_tree(self):
        self.assertFalse(self.b.search(10))


class TestInsertTree(unittest.TestCase):
    def setUp(self):
        self.b = BTree()

    def test_empty(self):
        self.b.insert(5, 'Five')
        self.assertEqual(self.b.root.elems[0][1], 'Five')

    def test_at_root(self):
        self.b.insert(5, 'Five')
        self.b.insert(4, 'Four')
        self.assertEqual(self.b.root.elems[0][1], 'Four')

    def test_new_level(self):
        self.b.insert(4, 'Four')
        self.b.insert(6, 'Six')
        self.b.insert(5, 'Five')
        self.assertEqual(self.b.root.elems[0][1], 'Five')
        self.assertIsNone(self.b.root.elems[1][1])
        self.assertEqual(self.b.root.left.elems[0][1], 'Four')
        self.assertIsNone(self.b.root.left.elems[1][1])
        self.assertEqual(self.b.root.right.elems[0][1], 'Six')
        self.assertIsNone(self.b.root.right.elems[1][1])

    def test_no_split(self):
        self.b.insert(4, 'Four')
        self.b.insert(2, 'Two')
        self.b.insert(6, 'Six')
        self.b.insert(8, 'Eight')
        self.b.insert(1, 'One')
        self.assertEqual(self.b.root.left.elems[0][1], 'One')
        self.assertEqual(self.b.root.right.elems[1][1], 'Eight')

    def test_split_node(self):
        self.b.insert(4, 'Four')
        self.b.insert(2, 'Two')
        self.b.insert(6, 'Six')
        self.b.insert(8, 'Eight')
        self.b.insert(1, 'One')
        self.b.insert(7, 'Seven')
        self.assertEqual(self.b.root.elems[0][1], 'Four')
        self.assertEqual(self.b.root.elems[1][1], 'Seven')
        self.assertEqual(self.b.root.mid.elems[0][1], 'Six')
        self.assertIsNone(self.b.root.mid.elems[1][1])
        self.assertEqual(self.b.root.right.elems[0][1], 'Eight')
        self.assertIsNone(self.b.root.right.elems[1][1])


class TestDeleteTree(unittest.TestCase):
    def setUp(self):
        self.b = BTree()

    def test_empty(self):
        pass

    def test_one_root(self):
        pass

    def test_two_root(self):
        pass

    def test_no_underflow(self):
        pass

    def test_underflow(self):
        pass

    def test_delete_level(self):
        pass


if __name__ == '__main__':
    unittest.main()
