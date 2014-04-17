from data_structures.stack import Stack


class Node(object):
    def __init__(self, key=None, val=None):
        self.elems = [(key, val), (None, None), (None, None), ]

    def __repr__(self):
        """For printing out the heap and its nodes
        It's here to save me typing during debugging"""
        result = "["
        for i in range(len(self.elems)):
            result += '%s, ' % str(self.elems[i])
        return '%s]' % result

    def add_to_node(self, key, val):
        pass

    def del_from_node(self, idx):
        pass

    def is_in_node(self, key):
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
