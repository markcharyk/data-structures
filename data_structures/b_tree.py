from data_structures.stack import Stack


class Node(object):
    def __init__(self, key=None, val=None):
        self.count = 0
        if key is not None:
            self.count = 1
        self.elems = [(key, val), (None, None), (None, None), ]
        self.children = []

    def __repr__(self):
        """For printing out the heap and its nodes
        It's here to save me typing during debugging"""
        result = "["
        for i in range(3):
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
        for i in range(3):
            if self.elems[i][0] == key:
                return True
        return False

    def split_node(self):
        return (
            Node(self.elems[0][0], self.elems[0][1]),
            self.elems[1],
            Node(self.elems[2][0], self.elems[2][1])
            )


class BTree(object):
    def __init__(self):
        self.root = Node()
        self.stack = Stack()

    def search(self, node, key):
        if node.has(key):
            if node.elems[0][0] == key:
                return node.elems[0][1]
            return node.elems[1][1]
        elif not node.children:
            raise MissingError
        elif key < node.elems[0][0]:
            return self.search(node.children[0], key)
        elif (node.count == 2 and key < node.elems[1][0]) or node.count == 1:
            return self.search(node.children[1], key)
        else:
            return self.search(node.children[2], key)

    # def insert(self, node, key, val):
    #     if node.has(key):
    #         self.stack = Stack()
    #         return
    #     self.stack.push(node)
    #     if node.left is not None and key < node.elems[0][0]:
    #         return self.insert(node.left, key, val)
    #     elif node.mid is not None and key < node.elems[1][0]:
    #         return self.insert(node.mid, key, val)
    #     elif node.right is not None:
    #         return self.insert(node.right, key, val)
    #     node.add_to_node(key, val)
    #     if node.count == 3:
    #         node = self._split(node)

    # def _split(self, node):
    #     new1, mid_elem, new2 = node.split_node()
    #     self.stack.pop()
    #     parent = self.stack.head
    #     parent.add_to_node(mid_elem[0], mid_elem[1])
    #     if mid_elem[0] < parent.elems[0][0] and parent.count == 2:
    #         parent.left, parent.mid = new1, new2

    def delete(self, key):
        pass


class MissingError(BaseException):
    pass
