# Created By Vasyl Paliy
# 2017

class Node():
    def __init__(self, key=None, element=None):
        self.key=key
        self.element=element
        self.next=None
        self.prev=None

class LRUCache():
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity <= 0")
        self.capacity=capacity
        self.head=None
        self.tail=None
        self.elements={}

    def _put(self, key, element):
        # if the cache is overloaded, delete the least used item
        if self.elements.has_key(key):
            node=self.elements[key]
            node.element=element
            self.__fix(node)
            return
        if len(self.elements) == self.capacity:
            # in case if the capacity size is 1 (preposterous)
            if self.tail is self.head:
                self.head=None
            victim = self.tail
            self.tail=self.tail.prev
            if self.tail:
                del self.tail.next
                self.tail.next=None
            # delete the least used element from the hash
            self.elements.pop(victim.key)
        node=Node(key, element)
        self.elements[key]=node
        if not self.head:
            self.head=self.tail=node
        else:
            self.head.prev=node
            node.next=self.head
            self.head=node

    def _get(self, key):
        if self.elements.has_key(key):
            value = self.elements[key]
            self.__fix(value)
            return value.element
        return -1

    def __fix(self, target):
        if target and target is not self.head:
            # if the node is in the middle, reassign its adjacent nodes
            if target is not self.tail:
                target.next.prev=target.prev
                target.prev.next=target.next
            target.next=self.head
            if target is self.tail:
                self.tail=self.tail.prev
                self.tail.next=None
            self.head.prev=target
            self.head=target
