import unittest
from data_structures.hasher import HashTable


class TestInit(unittest.TestCase):
    def test_small_list(self):
        ht = HashTable(32)
        self.assertEqual(ht.size(), 32)
        current = ht.head
        for i in xrange(32):
            self.assertEqual(current.val.id, i)
            current = current.next

    def test_big_list(self):
        ht = HashTable(1024)
        self.assertEqual(ht.size(), 1024)
        current = ht.head
        for i in xrange(1024):
            self.assertEqual(current.val.id, i)
            current = current.next


class TestHash(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(16)

    def test_non_string(self):
        with self.assertRaises(TypeError):
            self.ht.hash(100)

    def test_zero_word(self):
        self.assertEqual(self.ht.hash('pp'), 0)

    def test_one_word(self):
        self.assertEqual(self.ht.hash('ap'), 1)

    def test_middle_word(self):
        self.assertEqual(self.ht.hash('foo'), 4)

    def test_minus_one_word(self):
        self.assertEqual(self.ht.hash('op'), 15)


class TestSet(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(16)

    def test_empty_list(self):
        self.ht.set('foo', 324)
        current = self.ht.head
        while current.val.id != 4:
            current = current.next
        self.assertIsNotNone(current.val.search(('foo', 324)))

    def test_full_list(self):
        self.ht.set('a', 97)
        self.ht.set('b', 98)
        self.ht.set('c', 99)
        self.ht.set('d', 100)
        self.ht.set('e', 101)
        self.ht.set('f', 102)
        self.ht.set('g', 103)
        self.ht.set('h', 104)
        self.ht.set('i', 105)
        self.ht.set('j', 106)
        self.ht.set('k', 107)
        self.ht.set('l', 108)
        self.ht.set('m', 109)
        self.ht.set('n', 110)
        self.ht.set('o', 111)
        self.ht.set('p', 112)
        self.ht.set('foo', 324)
        current = self.ht.head
        while current.val.id != 4:
            current = current.next
        self.assertIsNotNone(current.val.search(('foo', 324)))


class TestGet(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(16)

    def test_empty_list(self):
        with self.assertRaises(KeyError):
            self.ht.get('foo')

    def test_full_list_error(self):
        self.ht.set('d', 100)
        with self.assertRaises(KeyError):
            self.ht.get('foo')

    def test_one_item_list(self):
        self.ht.set('foo', 324)
        self.assertEqual(self.ht.get('foo'), 324)

    def test_full_list(self):
        self.ht.set('a', 97)
        self.ht.set('b', 98)
        self.ht.set('c', 99)
        self.ht.set('d', 100)
        self.ht.set('e', 101)
        self.ht.set('f', 102)
        self.ht.set('g', 103)
        self.ht.set('h', 104)
        self.ht.set('i', 105)
        self.ht.set('j', 106)
        self.ht.set('k', 107)
        self.ht.set('l', 108)
        self.ht.set('m', 109)
        self.ht.set('n', 110)
        self.ht.set('o', 111)
        self.ht.set('p', 112)
        self.ht.set('foo', 324)
        self.assertEqual(self.ht.get('foo'), 324)


if __name__ == '__main__':
    unittest.main()
