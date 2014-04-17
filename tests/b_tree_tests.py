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
        self.b = BTree()

    def test_at_root(self):
        pass

    def test_in_middle(self):
        pass

    def test_at_leaf(self):
        pass

    def test_not_in_tree(self):
        pass


class TestInsertTree(unittest.TestCase):
    def setUp(self):
        self.b = BTree()

    def test_empty(self):
        pass

    def test_at_root(self):
        pass

    def test_no_split(self):
        pass

    def test_split_node(self):
        pass

    def test_new_level(self):
        pass


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
