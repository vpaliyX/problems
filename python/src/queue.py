from linked_list import Node

# Created By Vasy Paliy
# 2017

class Queue():
    def __init__(self):
        self.tail=None
        self.head=None
        self.size=0

    def _enqueue(self, data):
        target=Node(data)
        self.size+=1
        if self.head:
            target.prev=self.tail
            self.tail.next=target
            self.tail=target
        else:
            self.head=self.tail=target

    def _dequeue(self):
        if self.tail:
            result=self.tail.data
            if self.tail is self.head:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.prev
                self.tail.next=None
            return result
        raise BaseException("Queue is empty")

    def _is_empty(self):
        return self.tail != None
    
