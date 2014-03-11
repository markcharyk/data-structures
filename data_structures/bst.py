import random
import time


class BSTree(object):
    def __init__(self, *val):
        """Initialize a "leaf" of the tree to have a None value"""
        if val != ():
            self.val = val[0]
            self.left = BSTree()
            self.right = BSTree()
        else:
            self.val = None
            self.left = None
            self.right = None

    def __str__(self):
        """Return a string of all of the elements in the
        tree and its decendents in order"""
        result = ''
        if self.left.val is not None:
            result += str(self.left)
        result += "%s " % str(self.val)
        if self.right.val is not None:
            result += str(self.right)
        return result

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
        return max(self.left.depth() + 1, self.right.depth() + 1)

    def balance(self):
        """Return a value representing the balance of the tree"""
        if self.val is None:
            return 0
        return self.left.depth() - self.right.depth()

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
