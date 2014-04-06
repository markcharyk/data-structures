from random import shuffle


class Node(object):
    def __init__(self, val):
        self.left, self.right, self.parent = None, None, None
        self.balance = 0
        self.val = val


class AVLTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        self._insert(self.root, Node(val))

    def _insert(self, tree_node, new_node):
        if tree_node is None:
            self.root = new_node
        else:
            if new_node.val < tree_node.val:
                if tree_node.left is None:
                    tree_node.left = new_node
                    new_node.parent = tree_node
                    self.recursive_balance(tree_node)
                else:
                    self._insert(tree_node.left, new_node)
            elif new_node.val > tree_node.val:
                if tree_node.right is None:
                    tree_node.right = new_node
                    new_node.parent = tree_node
                    self.recursive_balance(tree_node)
                else:
                    self._insert(tree_node.right, new_node)

    def height(self, curr):
        if curr is None:
            return -1
        if curr.left is None and curr.right is None:
            return 0
        elif curr.left is None:
            return 1 + self.height(curr.right)
        elif curr.right is None:
            return 1 + self.height(curr.left)
        else:
            return 1 + max(self.height(curr.left), self.height(curr.right))

    def set_balance(self, curr):
        curr.balance = self.height(curr.right) - self.height(curr.left)

    def recursive_balance(self, curr):
        self.set_balance(curr)
        bal = curr.balance
        if bal == -2:
            if self.height(curr.left.left) >= self.height(curr.left.right):
                curr = self.rotate_right(curr)
            else:
                curr = self.rotate_left_right(curr)
        elif bal == 2:
            if self.height(curr.right.right) >= self.height(curr.right.left):
                curr = self.rotate_left(curr)
            else:
                curr = self.rotate_right_left(curr)
        if curr.parent is not None:
            self.recursive_balance(curr.parent)
        else:
            self.root = curr

    def remove(self, val):
        self._remove(self.root, val)

    def _remove(self, tree_node, val):
        if tree_node is None:
            return None
        else:
            if tree_node.val > val:
                self._remove(tree_node.left, val)
            elif tree_node.val < val:
                self._remove(tree_node.right, val)
            elif tree_node.val == val:
                self.remove_found_node(tree_node)

    def remove_found_node(self, found):
        temp = None
        if found.left is None or found.right is None:
            if found.parent is None:
                self.root = None
                found = None
                return None
        else:
            temp = self.succ(found)
            found.val = temp.key
        temp2 = None
        if temp.left is not None:
            temp2 = temp.left
        else:
            temp2 = temp.right
        if temp2 is not None:
            temp2.parent = temp.parent
        if temp.parent is None:
            self.root = temp2
        else:
            if temp == temp.parent.left:
                temp.parent.left = temp2
            else:
                temp.parent.right = temp2
            self.recursive_balance(temp.parent)
        temp = None

    def rotate_left(self, pivot):
        temp = pivot.right
        temp.parent = pivot.parent
        pivot.right = temp.left
        if pivot.right is not None:
            pivot.right.parent = pivot
        temp.left = pivot
        pivot.parent = temp

        if temp.parent is not None:
            if temp.parent.right is pivot:
                temp.parent.right = temp
            elif temp.parent.left is pivot:
                temp.parent.left = temp

        self.set_balance(pivot)
        self.set_balance(temp)
        return temp

    def rotate_right(self, pivot):
        temp = pivot.left
        temp.parent = pivot.parent
        pivot.left = temp.right
        if pivot.left is not None:
            pivot.left.parent = pivot
        temp.right = pivot
        pivot.parent = temp

        if temp.parent is not None:
            if temp.parent.right is pivot:
                temp.parent.right = temp
            elif temp.parent.left is pivot:
                temp.parent.left = temp

        self.set_balance(pivot)
        self.set_balance(temp)
        return temp

    def rotate_left_right(self, pivot):
        pivot.left = self.rotate_left(pivot.left)
        return self.rotate_right(pivot)

    def rotate_right_left(self, pivot):
        pivot.right = self.rotate_right(pivot.right)
        return self.rotate_left(pivot)

    def succ(self, curr):
        if curr.right is not None:
            temp = curr.right
            while temp.left is not None:
                temp = temp.left
        else:
            temp = curr.parent
            while temp is not None and curr is temp.right:
                curr = temp
                temp = curr.parent
        return temp
