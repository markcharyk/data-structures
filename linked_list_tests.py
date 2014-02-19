import unittest
import linked_list


class InitTest(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(linked_list.Linked_List.Node(10).val, 10)
        linked = linked_list.Linked_List()
        self.failUnlessEqual(linked.head, None)


class InsertTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        linked.insert(10)
        self.failUnlessEqual(linked.head.val, 10)

class PopTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        linked.insert(10)
        linked.insert(11)
        linked.insert(12)
        self.failUnlessEqual(linked.pop().val, 12)
        self.failUnlessEqual(linked.head.val, 11)


class SizeTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        self.failUnlessEqual(linked.size(), 0)
        linked.insert(10)
        linked.insert(11)
        linked.insert(12)
        self.failUnlessEqual(linked.size(), 3)


class SearchTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        self.failUnlessEqual(linked.search(10), None)
        linked.insert(10)
        linked.insert(11)
        linked.insert(12)
        self.failUnlessEqual(linked.search(10).val, 10)


class RemoveTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        self.failUnlessEqual(linked.remove(10), None)
        linked.insert(10)
        linked.insert(11)
        linked.insert(12)
        linked.remove(12)
        self.failUnlessEqual(linked.head.val, 11)
        linked.remove(10)
        self.failUnlessEqual(linked.size(), 1)
        linked.remove(10)
        self.failUnlessEqual(linked.size(), 1)


class StringTest(unittest.TestCase):
    def testEqual(self):
        linked = linked_list.Linked_List()
        self.failUnlessEqual(linked.__str__(), "()")
        linked.insert(10)
        linked.insert(11)
        linked.insert(12)
        self.failUnlessEqual(linked.__str__(), "(12, 11, 10)")

if __name__ == '__main__':
    unittest.main()
