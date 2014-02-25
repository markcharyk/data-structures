import unittest
import queue


class testEnqueue(unittest.TestCase):
    def setUp(self):
        self.q = queue.Queue()

    def testEmptyQueue(self):
        self.q.enqueue(10)
        self.assertEqual(self.q.head.val, 10)
        self.assertEqual(self.q.tail.val, 10)

    def testQueueOfOne(self):
        self.q.enqueue(10)
        self.q.enqueue(11)
        self.assertEqual(self.q.head.val, 11)
        self.assertEqual(self.q.tail.val, 10)

    def testLongQueue(self):
        self.q.enqueue(10)
        self.q.enqueue(11)
        self.q.enqueue(12)
        self.q.enqueue(13)
        self.q.enqueue(14)
        self.q.enqueue(15)
        self.assertEqual(self.q.head.val, 15)
        self.assertEqual(self.q.tail.val, 10)


class testDequeue(unittest.TestCase):
    def setUp(self):
        self.q = queue.Queue()

    def testEmptyQueue(self):
        self.assertRaises(IndexError, self.q.dequeue)

    def testQueueOfOne(self):
        self.q.enqueue(10)
        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.head, None)
        self.assertEqual(self.q.tail, None)

    def testLongQueue(self):
        self.q.enqueue(10)
        self.q.enqueue(11)
        self.q.enqueue(12)
        self.q.enqueue(13)
        self.q.enqueue(14)
        self.q.enqueue(15)
        self.assertEqual(self.q.dequeue(), 10)
        self.assertEqual(self.q.head.val, 15)
        self.assertEqual(self.q.tail.val, 11)
        self.assertEqual(self.q.dequeue(), 11)
        self.assertEqual(self.q.head.val, 15)
        self.assertEqual(self.q.tail.val, 12)


class testSize(unittest.TestCase):
    def setUp(self):
        self.q = queue.Queue()

    def testEmptyQueue(self):
        self.assertEqual(self.q.size(), 0)

    def testQueueOfOne(self):
        self.q.enqueue(10)
        self.assertEqual(self.q.size(), 1)
        self.q.dequeue()
        self.assertEqual(self.q.size(), 0)

    def testLongQueue(self):
        self.q.enqueue(10)
        self.q.enqueue(11)
        self.q.enqueue(12)
        self.q.enqueue(13)
        self.q.enqueue(14)
        self.q.enqueue(15)
        self.assertEqual(self.q.size(), 6)
        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(self.q.size(), 4)


if __name__ == '__main__':
    unittest.main()
