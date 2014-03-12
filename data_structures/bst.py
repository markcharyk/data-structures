import random
import time


class BSTree(object):
    def __init__(self, val=None):
        """Initialize a "leaf" of the tree to have a None value"""
        self.val = val
        if val is not None:
            self.left = BSTree()
            self.right = BSTree()
        else:
            self.left = None
            self.right = None

    def insert(self, val):
        """Insert a value below the root of the tree"""
        if self.val is None:
            self.__init__(val)
        elif self.val > val:
            self.left.insert(val)
        elif self.val < val:
            self.right.insert(val)

    def contains(self, val):
        """Return whether the item is contained in the tree"""
        if self.val is None:
            return False
        elif self.val == val:
            return True
        elif self.val > val:
            return self.left.contains(val)
        return self.right.contains(val)

    def size(self):
        """Return the size of the tree"""
        count = 0
        if self.val is None:
            return count
        else:
            count += 1
        count += self.left.size()
        count += self.right.size()
        return count

    def depth(self):
        """Return the maximum depth of the tree"""
        result = 0
        if self.val is None:
            return result
        return max(self.left.depth(), self.right.depth()) + 1

    def balance(self):
        """Return a value representing the balance of the tree"""
        if self.val is None:
            return 0
        return self.left.depth() - self.right.depth()

    def in_order(self):
        """Return a generator that lists the elements in order"""
        if self.left is not None:
            for i in self.left.in_order():
                yield i
        if self.val is not None:
            yield self.val
        if self.right is not None:
            for i in self.right.in_order():
                yield i

    def pre_order(self):
        """Return a generator that lists the elements from the root downward"""
        if self.val is not None:
            yield self.val
        if self.left is not None:
            for i in self.left.pre_order():
                yield i
        if self.right is not None:
            for i in self.right.pre_order():
                yield i

    def post_order(self):
        """Return a generator that lists the elements
        from the children upward"""
        if self.left is not None:
            for i in self.left.post_order():
                yield i
        if self.right is not None:
            for i in self.right.post_order():
                yield i
        if self.val is not None:
            yield self.val

    def breadth_first(self):
        """Return a generator that lists the elements
        in a breadth first order"""
        import queue
        keeper, result = queue.Queue(), []
        keeper.enqueue(self)
        while(keeper.size() != 0):
            temp = keeper.dequeue()
            result.append(temp.val)
            if temp.left is not None:
                keeper.enqueue(temp.left)
            if temp.right is not None:
                keeper.enqueue(temp.right)
        return (x for x in result if x is not None)

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.val is None else (
            "\t%s;\n%s\n" % (
                self.val,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.val, self.left.val)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.val, self.right.val)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)


if __name__ == '__main__':
    b1 = BSTree()
    b2 = BSTree()
    for i in xrange(512):
        b1.insert(random.choice(range(4096)))
        b2.insert(i)
    t1 = time.time()
    is_in_b1 = b1.contains(500)
    t2 = time.time()
    is_in_b2 = b2.contains(500)
    t3 = time.time()
    print "Random case: %f seconds" % (t2 - t1)
    print "Worst case: %f seconds" % (t3 - t2)
    b3 = BSTree()
    b3.insert(2)
    b3.insert(5)
    b3.insert(1)
    b3.insert(8)
    b3.insert(3)
    for i in b3.post_order():
        print i
