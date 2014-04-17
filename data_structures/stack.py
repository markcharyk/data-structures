class Stack(object):

    def __init__(self, *args):
        self.head = None
        if len(args) > 0:
            for n in xrange(len(args)):
                self.push(args[n])

    def __str__(self):
        h = self.head
        if not h:
            h = "empty"
        return "The head is %s, who knows what else is underneath it?" % h

    def push(self, val):
        old_head, self.head = self.head, Node(val)
        self.head.next = old_head

    def pop(self):
        if not self.head:
            raise IndexError
        result, self.head = self.head, self.head.next
        return result


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
