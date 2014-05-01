import unittest
from data_structures.b_tree import Node, BTree, MissingError, InvalidDegreeError


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


class TestInitTree(unittest.TestCase):
    def test_degree_two(self):
        b = BTree()
        self.assertIsNone(b.root.elems[0][0])

    def test_degree_one(self):
        with self.assertRaises(InvalidDegreeError):
            BTree(1)

    def test_degree_four(self):
        b = BTree(4)
        self.assertIsNone(b.root.elems[0][0])


class TestSearchTree(unittest.TestCase):
    def setUp(self):
        four = Node(4, 'Four')
        two = Node(2, 'Two')
        four.children[0] = two
        six_eight = Node(6, 'Six')
        six_eight.add_to_node(8, 'Eight')
        four.children[1] = six_eight
        one = Node(1, 'One')
        three = Node(3, 'Three')
        two.children[0] = one
        two.children[1] = three
        five = Node(5, 'Five')
        seven = Node(7, 'Seven')
        nine = Node(9, 'Nine')
        six_eight.children[0] = five
        six_eight.children[1] = seven
        six_eight.children[2] = nine
        self.b = BTree()
        self.b.root = four

    def test_at_root(self):
        self.assertEqual(self.b.search(self.b.root, 4), (self.b.root, 0))

    def test_in_middle(self):
        self.assertEqual(self.b.search(self.b.root, 2), (self.b.root.children[0], 0))
        self.assertEqual(self.b.search(self.b.root, 8), (self.b.root.children[1], 1))

    def test_at_leaf(self):
        self.assertEqual(self.b.search(self.b.root, 1), (self.b.root.children[0].children[0], 0))
        self.assertEqual(self.b.search(self.b.root, 9), (self.b.root.children[1].children[2], 0))

    def test_not_in_tree(self):
        with self.assertRaises(MissingError):
            self.b.search(self.b.root, 10)


class TestSplitChild(unittest.TestCase):
    def setUp(self):
        self.b = BTree()
        self.b.root.add_to_node(4, 'Four')

    def test_right_split(self):
        m, n = Node(), Node()
        m.add_to_node(1, 'One')
        n.add_to_node(5, 'Five')
        n.add_to_node(7, 'Seven')
        n.add_to_node(9, 'Nine')
        self.b.root.children[0], self.b.root.children[1] = m, n
        self.b._split_child(self.b.root, self.b.root.children[1])
        self.assertEqual(self.b.root.elems[0][1], 'Four')
        self.assertEqual(self.b.root.elems[1][1], 'Seven')
        self.assertEqual(self.b.root.children[1].elems[0][1], 'Five')
        self.assertIsNone(self.b.root.children[1].elems[1][1])
        self.assertEqual(self.b.root.children[2].elems[0][1], 'Nine')

    def test_left_split(self):
        m, n = Node(), Node()
        m.add_to_node(1, 'One')
        m.add_to_node(2, 'Two')
        m.add_to_node(3, 'Three')
        n.add_to_node(9, 'Nine')
        self.b.root.children[0], self.b.root.children[1] = m, n
        self.b._split_child(self.b.root, self.b.root.children[0])
        self.assertEqual(self.b.root.elems[0][1], 'Two')
        self.assertEqual(self.b.root.elems[1][1], 'Four')
        self.assertEqual(self.b.root.children[0].elems[0][1], 'One')
        self.assertIsNone(self.b.root.children[0].elems[1][1])
        self.assertEqual(self.b.root.children[1].elems[0][1], 'Three')
        self.assertEqual(self.b.root.children[2].elems[0][1], 'Nine')

    def test_with_children(self):
        m, n, o, p, q, r, s = Node(), Node(), Node(), Node(), Node(), Node(), Node()
        m.add_to_node(2, 'Two')
        n.add_to_node(6, 'Six')
        n.add_to_node(8, 'Eight')
        self.b.root.children[0], self.b.root.children[1] = m, n
        o.add_to_node(1, 'One')
        p.add_to_node(3, 'Three')
        self.b.root.children[0].children[0], self.b.root.children[0].children[1] = o, p
        q.add_to_node(5, 'Five')
        r.add_to_node(7, 'Seven')
        s.add_to_node(9, 'Nine')
        s.add_to_node(10, 'Ten')
        s.add_to_node(11, 'Eleven')
        self.b.root.children[1].children[0], self.b.root.children[1].children[1] = q, r
        self.b.root.children[1].children[2] = s
        self.b._split_child(self.b.root.children[1], self.b.root.children[1].children[2])
        self.b._split_child(self.b.root, self.b.root.children[1])
        self.assertEqual(self.b.root.elems[1][1], 'Eight')
        self.assertIsNone(self.b.root.elems[2][1])
        self.assertEqual(self.b.root.children[1].elems[0][1], 'Six')
        self.assertIsNone(self.b.root.children[1].elems[1][1])
        self.assertEqual(self.b.root.children[2].elems[0][1], 'Ten')
        self.assertIsNone(self.b.root.children[2].elems[1][1])
        self.assertEqual(self.b.root.children[1].children[0].elems[0][1], 'Five')
        self.assertEqual(self.b.root.children[1].children[1].elems[0][1], 'Seven')
        self.assertIsNone(self.b.root.children[1].children[2])
        self.assertEqual(self.b.root.children[2].children[0].elems[0][1], 'Nine')
        self.assertEqual(self.b.root.chidlren[2].children[1].elems[0][1], 'Eleven')
        self.assertIsNone(self.b.root.children[2].children[2])


# class TestInsertTree(unittest.TestCase):
#     def setUp(self):
#         self.b = BTree()

#     def test_empty(self):
#         self.b.insert(self.b.root, 5, 'Five')
#         self.assertEqual(self.b.root.elems[0][1], 'Five')

#     def test_at_root(self):
#         self.b.insert(self.b.root, 5, 'Five')
#         self.b.insert(self.b.root, 4, 'Four')
#         self.assertEqual(self.b.root.elems[0][1], 'Four')

#     def test_new_level(self):
#         self.b.insert(self.b.root, 4, 'Four')
#         self.b.insert(self.b.root, 6, 'Six')
#         self.b.insert(self.b.root, 5, 'Five')
#         self.assertEqual(self.b.root.elems[0][1], 'Five')
#         self.assertIsNone(self.b.root.elems[1][1])
#         self.assertEqual(self.b.root.children[0].elems[0][1], 'Four')
#         self.assertIsNone(self.b.root.children[0].elems[1][1])
#         self.assertEqual(self.b.root.children[1].elems[0][1], 'Six')
#         self.assertIsNone(self.b.root.children[1].elems[1][1])

#     def test_no_split(self):
#         self.b.insert(self.b.root, 4, 'Four')
#         self.b.insert(self.b.root, 2, 'Two')
#         self.b.insert(self.b.root, 6, 'Six')
#         self.b.insert(self.b.root, 8, 'Eight')
#         self.b.insert(self.b.root, 1, 'One')
#         self.assertEqual(self.b.root.children[0].elems[0][1], 'One')
#         self.assertEqual(self.b.root.children[1].elems[1][1], 'Eight')

#     def test_split_node(self):
#         self.b.insert(self.b.root, 4, 'Four')
#         self.b.insert(self.b.root, 2, 'Two')
#         self.b.insert(self.b.root, 6, 'Six')
#         self.b.insert(self.b.root, 8, 'Eight')
#         self.b.insert(self.b.root, 1, 'One')
#         self.b.insert(self.b.root, 7, 'Seven')
#         self.assertEqual(self.b.root.elems[0][1], 'Four')
#         self.assertEqual(self.b.root.elems[1][1], 'Seven')
#         self.assertEqual(self.b.root.children[1].elems[0][1], 'Six')
#         self.assertIsNone(self.b.root.children[1].elems[1][1])
#         self.assertEqual(self.b.root.children[2].elems[0][1], 'Eight')
#         self.assertIsNone(self.b.root.children[2].elems[1][1])


# class TestDeleteTree(unittest.TestCase):
#     def setUp(self):
#         self.b = BTree()

#     def test_empty(self):
#         with self.assertRaises(MissingError):
#             self.b.delete(4)

#     def test_one_root(self):
#         self.b.insert(4, 'Four')
#         self.b.delete(4)
#         with self.assertRaises(MissingError):
#             self.b.search(4)

#     def test_two_root(self):
#         self.b.insert(4, 'Four')
#         self.b.insert(5, 'Five')
#         self.b.delete(4)
#         self.assertEqual(self.b.root.elems[0][1], 'Five')
#         self.assertIsNone(self.b.root.elems[1][1])

#     def test_no_underflow(self):
#         self.b.insert(4, 'Four')
#         self.b.insert(2, 'Two')
#         self.b.insert(6, 'Six')
#         self.b.insert(8, 'Eight')
#         self.b.insert(1, 'One')
#         self.b.delete(6)
#         self.assertEqual(self.b.root.right.elems[0][1], 'Eight')
#         self.assertIsNone(self.b.root.right.elems[1][1])

#     def test_underflow(self):
#         self.b.insert(1, 'One')
#         self.b.insert(2, 'Two')
#         self.b.insert(3, 'Three')
#         self.b.insert(4, 'Four')
#         self.b.insert(5, 'Five')
#         self.b.insert(6, 'Six')
#         self.b.insert(7, 'Seven')
#         self.b.insert(8, 'Eight')
#         self.b.insert(9, 'Nine')
#         self.b.delete(8)
#         self.assertEqual(self.b.root.right.elems[0][1], 'Seven')
#         self.assertIsNone(self.b.root.right.elems[1][1])
#         self.assertEqual(self.b.root.right.left.elems[0][1], 'Five')
#         self.assertEqual(self.b.root.right.left.elems[1][1], 'Six')
#         self.assertIsNone(self.b.root.right.mid)
#         self.assertEqual(self.b.root.right.right.elems[0][1], 'Nine')
#         self.assertIsNone(self.b.root.right.right.elems[1][1])

#     def test_delete_level(self):
#         self.b.insert(4, 'Four')
#         self.b.insert(2, 'Two')
#         self.b.insert(6, 'Six')
#         self.b.delete(6)
#         self.assertEqual(self.root.elems[0][1], 'Two')
#         self.assertEqual(self.root.elems[1][1], 'Four')
#         self.assertIsNone(self.root.left)
#         self.assertIsNone(self.root.right)


if __name__ == '__main__':
    unittest.main()
