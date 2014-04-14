class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Heap(object):
    def __init__(self):
        self.heap = []

    def insert(self, key, val):
        self.heap.append(Node(key, val))
        self._upheap(len(self.heap) - 1)

    def _upheap(self, idx):
        pass

    def delete_min(self):
        if self.heap:
            return self.heap.pop().val

    def _downheap(self, idx):
        pass
