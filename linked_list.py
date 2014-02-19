class Linked_List(object):

    def __init__(self, *args):
        self.head = None
        if len(args) == 0:
            return None
        elif len(args) > 0:
            self.head = args[0]
            return None
        for n in xrange(len(args[:-1])):
            args[n].next = args[n+1]

    class Node(object):

        def __init__(self, val):
            self.val = val
            self.next = None

        def __str__(self):
            return str(self.val)

    def insert(self, val):
        new = self.Node(val)
        new.next = self.head
        self.head = new

    def pop(self):
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
        trail = self.head
        if self.head.val == val:
            self.head = self.head.next
        while ptr:
            if ptr.val == val:
                trail.next = ptr.next
                return None
            trail = ptr
            ptr = ptr.next
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


if __name__ == '__main__':
    my_ll = Linked_List()
    print my_ll
    my_ll.insert(15)
    my_ll.insert(16)
    my_ll.insert(15)
    print my_ll
    my_ll.remove(15)
    print my_ll
