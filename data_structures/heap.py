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
        self.heap.append(Node(key, val))
        self._upheap(len(self.heap) - 1)

    def _upheap(self, idx):
        if idx > 0:
            if self.heap[(idx-1) // 2].key > self.heap[idx].key:
                self.heap[(idx-1) // 2], self.heap[idx] = \
                    self.heap[idx], self.heap[(idx-1) // 2]
                self._upheap((idx-1) // 2)

    def delete_min(self):
        # import pdb; pdb.set_trace()
        if self.heap:
            if len(self.heap) == 1:
                return self.heap.pop().val
            temp = self.heap.pop()
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            self._downheap(0)
            return temp.val

    def _downheap(self, idx):
        new = 0
        if 2 * idx + 2 < len(self.heap):
            if self.heap[2 * idx + 2].key <= self.heap[2 * idx + 1].key:
                new = 2 * idx + 2
            else:
                new = 2 * idx + 1
        elif 2 * idx + 1 < len(self.heap):
            new = 2 * idx + 1
        # if new = 0 here, the node has no "children"
        if new and self.heap[idx].key > self.heap[new].key:
            self.heap[idx], self.heap[new] = self.heap[new], self.heap[idx]
            self._downheap(new)
