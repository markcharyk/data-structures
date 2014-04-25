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
        """Searches the tree for a specific key and returns
        the associated value if it is found
        If it is not found, raises a custom error"""
        if node.has(key):
            if node.elems[0][0] == key:
                return node.elems[0][1]
            return node.elems[1][1]
        elif not node.children:
            # The search has reached a leaf node w/o finding a match
            raise MissingError
        elif key < node.elems[0][0]:
            return self.search(node.children[0], key)
        # Check if a middle child exists
        elif (node.count == 2 and key < node.elems[1][0]) or node.count == 1:
            return self.search(node.children[1], key)
        else:
            # A third child exists
            return self.search(node.children[2], key)

    def insert(self, node, key, val):
        """Inserts a key-value pair into the tree
        No-op if the key already exists"""
        self.stack.push(node)
        if node.has(key):
            self.stack = Stack()
            return
        elif not node.children:
            node.add_to_node(key, val)
            if node.count == 3:
                self._split(node)
            self.stack = Stack()
            return
        elif key < node.elems[0][0]:
            return self.insert(node.children[0], key, val)
        elif (node.count == 2 and key < node.elems[1][0]) or node.count == 1:
            return self.insert(node.children[1], key, val)
        else:
            return self.insert(node.children[2], key, val)

    def _split(self, node):
        new1, mid_elem, new2 = node.split_node()
        self.stack.pop()
        if self.stack.head:
            parent = self.stack.head.val
            parent.children.remove(node)
        else:
            parent = Node()
            self.root = parent
        parent.add_to_node(mid_elem[0], mid_elem[1])
        parent.children.extend([new1, new2])
        parent.children.sort(key=lambda nod: nod.elems[0][0])
        if node.children:
            new1.children, new2.children = \
                node.children[:2], node.children[-2:]
        if parent.count == 3:
            self._split(parent)

    def delete(self, node, key):
        self.stack.push(node)
        if node.has(key) and not node.children:
            # Node is a leaf
            if key == node.elems[0][0]:
                node.del_from_node(0)
            else:
                node.del_from_node(1)
            if not node.count:
                # Node is newly empty
                self.stack.head.next.val.children = [x for x in self.stack.head.next.val.children if x.elems[0][0] is not None]
                self._pull_down(node)
            return
        elif node.has(key):
            if key == node.elems[0][0]:
                node.elems[0] = self._get_pred(node, key)
            else:
                node.elems[1] = self._get_pred(node, key)

    def _get_pred(self, node, key):
        if node.elems[0][0] == key:
            next_node = node.children[0]
        else:
            next_node = node.children[1]
        while next_node.children:
            self.stack.push(next_node)
            next_node = next_node.children[-1]
        result = next_node.elems[next_node.count - 1]
        self.delete(next_node, next_node.elems[next_node.count - 1][0])
        return result

    def _pull_down(self, node):
        pass

    def _transfer(self, parent, child):
        pass

    def _fuse(self, node1, node2):
        pass


class MissingError(BaseException):
    pass


def set_up(tree):
    tree.insert(tree.root, 1, 1)
    tree.insert(tree.root, 2, 2)
    tree.insert(tree.root, 3, 3)
    tree.insert(tree.root, 4, 4)
    tree.insert(tree.root, 5, 5)
    tree.insert(tree.root, 6, 6)
    tree.insert(tree.root, 7, 7)
    tree.insert(tree.root, 8, 8)
    tree.insert(tree.root, 9, 9)
    tree.insert(tree.root, 10, 10)
