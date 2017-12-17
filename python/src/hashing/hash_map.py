# Created By Vasyl Paliy
# 2017

class Entry():
    def __init__(self, key=None, value=None, next=None):
        self.key=key
        self.value=value
        self.next=next

class HashTable():
    def __init__(self, capacity=10):
        self.capacity=capacity
        self.array=[]

    def get(self, key):
        if key:
            index=self._hash(key)
            node = self.array[index]
            while node:
                if node.key == key:
                    return node.value
                node=node.next
        return None

    def put(self, key, value):
        if len(self.array) >= self.capacity:
            self.capacity+=10
        index = self._hash(key)
        node = self.array[index]
        target = Entry(key, value)
        if not node:
            self.array[index]=target
        else:
            while node.next:
                node=node.next
            node.next=target

    def _hash(self, key):
        return sum([ord(c) for c in key]) % self.capacity
