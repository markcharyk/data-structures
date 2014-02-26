from linked_list import Linked_List


class Bucket(Linked_List):
    def __init__(self, id):
        super(Bucket, self).__init__()
        self.id = id


class HashTable(Linked_List):
    def __init__(self, buckets):
        self.buckets = buckets
        super(HashTable, self).__init__()
        for i in xrange(buckets - 1, -1, -1):
            self.insert(Bucket(i))

    def hash(self, key):
        result = 0
        for char in key:
            result += ord(char)
        return result % self.buckets

    def set(self, key, val):
        try:
            hash_val = self.hash(key)
        except TypeError:
            raise ValueError("OK but try with a string this time")
        current = self.find_bucket(hash_val)
        if current.val.search((key, val)):
            return
        current.val.insert((key, val))

    def get(self, key):
        try:
            hash_val = self.hash(key)
        except TypeError:
            raise ValueError("OK but try with a string this time")
        current = self.find_bucket(hash_val).val.head
        while current and current.val[0] != key:
            current = current.next
        if current:
            return current.val[1]
        else:
            raise KeyError("I'm sorry, I don't have anything by that name")

    def find_bucket(self, hash_val):
        current = self.head
        while current and current.val.id != hash_val:
            current = current.next
        return current
