class Linked_List(object):

    def __init__(self, *args):
        self.head = None
        if len(args) == 0:
            return None
        elif len(args) > 0:
            for n in xrange(len(args)):
                self.insert(args[n])

    def insert(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return None
        result = self.head
        self.head = self.head.next
        return result

    def size(self):
        count = 0
        ptr = self.head
        while ptr:
            count += 1
            ptr = ptr.next
        return count

    def search(self, val):
        ptr = self.head
        while ptr:
            if ptr.val == val:
                return ptr
            ptr = ptr.next
        return None

    def remove(self, val):
        if not self.head:
            return None
        ptr = self.head
        if ptr.val == val:
            self.head = self.head.next
            return None
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
                return None

    def __str__(self):
        if not self.head:
            return "()"
        accu = "(" + str(self.head) + ", "
        ptr = self.head
        while ptr.next:
            accu += str(ptr.next) + ", "
            ptr = ptr.next
        return accu[:-2] + ")"


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)
