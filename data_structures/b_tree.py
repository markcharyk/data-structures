from data_structures.stack import Stack


class Node(object):
    def __init__(self, key=None, val=None):
        self.count = 0
        if key is not None:
            self.count = 1
        self.elems = [(key, val), (None, None), (None, None), ]
        self.children = [None] * 4

    def __repr__(self):
        """For printing out the nodes
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

    def sort_children(self):
        self.children.sort(key=lambda nod: nod.elems[0][0] if nod else None)
        while self.children[0] is None:
            self.children.pop(0)
            self.children.append(None)


class BTree(object):
    def __init__(self, degree=2):
        self.root = Node()
        self.stack = Stack()
        if degree < 2:
            raise InvalidDegreeError
        self.degree = degree

    def __repr__(self):
        """For printing out the tree and its nodes
        It's here to save me typing during debugging"""
        result = ''
        for i in self._bft():
            result += i
        return result

    def _bft(self):
        import queue
        keeper = queue.Queue()
        keeper.enqueue(self.root)
        while keeper.size() > 0:
            temp = keeper.dequeue()
            yield str(temp)
            if temp is not '\n' and temp.children[0]:
                keeper.enqueue('\n')
                for nod in temp.children:
                    if nod is not None:
                        keeper.enqueue(nod)

    def search(self, key):
        """Returns the value of the searched-for key"""
        nod, idx = self._recursive_search(self.root, key)
        return nod.elems[idx][1]

    def _recursive_search(self, node, key):
        """Searches the subtree for a specific key and returns
        where to find it if it is found
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
            return self._recursive_search(node.children[idx], key)

    def insert(self, key, val):
        """Inserts a key-value pair into the tree"""
        self._recursive_insert(self.root, key, val)

    def _split_child(self, parent, child):
        new = Node()
        for i in xrange(self.degree-1):
            new.add_to_node(*child.elems[i+self.degree])
            child.del_from_node(i+self.degree)
        parent.add_to_node(*child.elems[self.degree-1])
        child.del_from_node(self.degree-1)
        if child.children[0]:
            for i in xrange(self.degree):
                new.children[i], child.children[i+self.degree] = \
                    child.children[i+self.degree], None
            child.sort_children
        parent.children[2*self.degree-1] = new
        parent.sort_children()
        if parent.count == 2 * self.degree - 1:
            self._split_child(self.stack.pop().val, parent)

    def _recursive_insert(self, node, key, val):
        if not node.children[0]:
            node.add_to_node(key, val)
            if node.count == 2 * self.degree - 1:
                if node is self.root:
                    new = Node()
                    new.children[0], self.root = self.root, new
                    self.stack.push(new)
                self._split_child(self.stack.pop().val, node)
        else:
            self.stack.push(node)
            idx = node.count - 1
            while idx >= 0 and key < node.elems[idx][0]:
                idx -= 1
            self._recursive_insert(node.children[idx+1], key, val)


    def delete(self, key):
        self._recursive_delete(self.root, key)

    def _recursive_delete(self, node, key):
        pass

    def _move_key(self, key, src, dest):
        pass

    def _merge_nodes(self, node1, node2):
        pass

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


class InvalidDegreeError(BaseException):
    pass


class MissingError(BaseException):
    pass
