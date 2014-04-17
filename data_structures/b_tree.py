from data_structures.stack import Stack


class Node(object):
    def __init__(self, key=None, val=None):
        self.count = 0
        if key is not None:
            self.count = 1
        self.elems = [(key, val), (None, None), (None, None), ]

    def __repr__(self):
        """For printing out the heap and its nodes
        It's here to save me typing during debugging"""
        result = "["
        for i in range(self.count):
            result += '%s, ' % str(self.elems[i])
        return '%s]' % result

    def add_to_node(self, key, val):
        for i in range(3):
            if self.elems[i][0] is None or self.elems[i][0] > key:
                self.elems.pop()
                self.elems.insert(i, (key, val))
                self.count += 1
                break

    def del_from_node(self, idx):
        self.elems.pop(idx)
        self.count -= 1
        self.elems.append((None, None))

    def has(self, key):
        pass

    def split_node(self):
        pass


class BTree(object):
    def __init__(self):
        self.root = Node()

    def search(self, key):
        pass

    def insert(self, key, val):
        pass

    def delete(self, key):
        pass
