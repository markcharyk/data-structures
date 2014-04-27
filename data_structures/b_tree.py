from data_structures.stack import Stack


class Node(object):
    def __init__(self, key=None, val=None):
        self.count = 0
        if key is not None:
            self.count = 1
        self.elems = [(key, val), (None, None), (None, None), ]
        self.children = [None] * 3

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

    def is_legal(self):
        """Determines if an internal node is legal"""
        if self.children[0] is not None and self.children[1] is not None:
            if self.count == 1 and self.children[2] is None:
                return True
            elif self.count == 2 and self.children[2] is not None:
                return True
        return False


class BTree(object):
    def __init__(self):
        self.root = Node()
        self.stack = Stack()

    def search(self, node, key):
        """Searches the tree for a specific key and returns
        the associated value if if is found
        If it is not found, raises a custom error"""
        # The index of the node in which the key is found
        idx = 0
        while idx <= node.count - 1 and key > node.elems[idx][0]:
            # Look to the next key in the node
            idx += 1
        if idx <= node.count - 1 and key == node.elems[idx][0]:
            # Found the key in the node
            return node, idx
        if not node.children[0]:
            raise MissingError
        else:
            # Look to the appropriate child
            return self.search(node.children[idx], key)

    def insert(self, node, key, val):
        """Inserts a key-value pair into the tree"""
        r = self.root
        if node.count == 3:
            new = Node()
            self.root = new
            new.left = node
            self._split_child(new, node, 0)
            self._insert_nonfull(new, key)
        else:
            self._insert_nonfull(node, key)

    def _split_child(self, parent, child, idx):
        pass

    def _insert_nonfull(self, node, key)

    # def search(self, node, key):
    #     """Searches the tree for a specific key and returns
    #     the associated value if it is found
    #     If it is not found, raises a custom error"""
    #     if node.has(key):
    #         if node.elems[0][0] == key:
    #             return node.elems[0][1]
    #         return node.elems[1][1]
    #     elif not node.left:
    #         # The search has reached a leaf node w/o finding a match
    #         raise MissingError
    #     elif key < node.elems[0][0]:
    #         return self.search(node.left, key)
    #     # Check if a 3-node
    #     elif node.count == 2 and key > node.elems[1][0]:
    #         return self.search(node.right, key)
    #     else:
    #         return self.search(node.mid, key)

    # def insert(self, node, key, val):
    #     """Inserts a key-value pair into the tree
    #     No-op if the key already exists"""
    #     self.stack.push(node)
    #     if node.has(key):
    #         self.stack = Stack()
    #         return
    #     elif not node.first:
    #         node.add_to_node(key, val)
    #         if node.count == 3:
    #             self._split(node)
    #         self.stack = Stack()
    #         return
    #     elif key < node.elems[0][0]:
    #         return self.insert(node.first, key, val)
    #     # Check if a 3-node
    #     elif node.count == 2 and key > node.elems[1][0]:
    #         return self.insert(node.third, key, val)
    #     else:
    #         return self.insert(node.second, key, val)

    # def _split(self, node):
    #     new1, mid_elem, new2 = node.split_node()
    #     self.stack.pop()
    #     if self.stack.head:
    #         parent = self.stack.head.val
    #         parent.children.remove(node)
    #     else:
    #         parent = Node()
    #         self.root = parent
    #     parent.add_to_node(mid_elem[0], mid_elem[1])
    #     parent.children.extend([new1, new2])
    #     parent.children.sort(key=lambda nod: nod.elems[0][0])
    #     if node.children:
    #         new1.children, new2.children = \
    #             node.children[:2], node.children[-2:]
    #     if parent.count == 3:
    #         self._split(parent)

    # def delete(self, node, key):
    #     self.stack.push(node)
    #     if node.has(key) and not node.children:
    #         # Node is a leaf
    #         if key == node.elems[0][0]:
    #             node.del_from_node(0)
    #         else:
    #             node.del_from_node(1)
    #         if not node.count:
    #             # Node is newly empty
    #             self._borrow(node, self.stack.head.next.val)
    #             self.stack.head.next.val.children = [x for x in self.stack.head.next.val.children if x.elems[0][0] is not None]
    #         return
    #     elif node.has(key):
    #         if key == node.elems[0][0]:
    #             node.elems[0] = self._get_pred(node, key)
    #         else:
    #             node.elems[1] = self._get_pred(node, key)

    # def _get_pred(self, node, key):
    #     if node.elems[0][0] == key:
    #         next_node = node.children[0]
    #     else:
    #         next_node = node.children[1]
    #     while next_node.children:
    #         self.stack.push(next_node)
    #         next_node = next_node.children[-1]
    #     result = next_node.elems[next_node.count - 1]
    #     self.delete(next_node, next_node.elems[next_node.count - 1][0])
    #     return result

    # def _borrow(self, node, parent):
    #     elements = [x for x in parent.elems if x[0] is not None]
    #     elements.extend([y.elems[0] for y in parent.children if y.elems[0][0] is not None])
    #     elements.extend([y.elems[1] for y in parent.children if y.elems[1][0] is not None])
    #     elements.sort(key=lambda elem: elem[0])
    #     parent.del_from_node(0)
    #     parent.del_from_node(1)
    #     if len(elements) >= 5:
    #         # The parent can stay a 3-node
    #         parent.add_to_node(elements[1][0], elements[1][1])
    #         parent.add_to_node(elements[3][0], elements[3][1])
    #         parent.children = [Node(elements[0]), Node(elements[2]), Node(elements[4])]
    #         if len(elements) == 6:
    #             parent.children[2].add_to_node(elements[5][0], elements[5][1])
    #     elif len(elements) >= 3:
    #         # The group has all the keys it needs
    #         parent.add_to_node(elements[1][0], elements[1][1])
    #         parent.children = [Node(elements[0]), Node(elements[2])]
    #         if len(elements) == 4:
    #             parent.children[1].add_to_node(elements[3][0], elements[3][1])
    #     else:
    #         # Group needs to get a key from above
    #         pass


class MissingError(BaseException):
    pass
