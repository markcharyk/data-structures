class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        # Returned in reverse order so first element to be dequeued
        # would be the element at the "front" of the line of values
        current, result = self.tail, ''
        while current:
            result += str(current)
            current = current.prev

    def enqueue(self, val):
        old_head, self.head = self.head, Node(val)
        self.head.next = old_head
        if old_head:
            old_head.prev = self.head
        else:
            self.tail = self.head

    def dequeue(self):
        if not self.head:
            raise IndexError
        result, self.tail = self.tail, self.tail.prev
        result.prev = None
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return result.val

    def size(self):
        current, result = self.head, 0
        while current:
            result += 1
            current = current.next
        return result


class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.val)
