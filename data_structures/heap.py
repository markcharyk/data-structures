class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return "(%d, %s)" % (self.key, self.val)


class Heap(object):
    def __init__(self):
        self.heap = []

    def insert(self, key, val):
        # import pdb; pdb.set_trace()
        self.heap.append(Node(key, val))
        self._upheap(len(self.heap) - 1)

    def _upheap(self, idx):
        if idx > 0:
            if self.heap[(idx-1) // 2].key > self.heap[idx].key:
                self.heap[(idx-1) // 2], self.heap[idx] = \
                    self.heap[idx], self.heap[(idx-1) // 2]
                self._upheap((idx-1) // 2)

    def delete_min(self):
        if self.heap:
            return self.heap.pop().val

    def _downheap(self, idx):
        pass
