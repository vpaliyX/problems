from linked_list import Node

# Created By Vasyl Paliy
# 2017

class Stack():
    def __init__(self):
        self.head=None
        self.size=0

    def _push(self, item):
        target=Node(item)
        if self.head:
            target.next=self.head
        self.head=target
        self.size+=1

    def _pop(self):
        if self.head:
            self.size-=1
            element=self.head.data
            self.head=self.head.next
            return element
        raise BaseException("Stack is empty!")

    def __repr__(self):
        result=''
        node=self.head
        while node:
            result+='%s' % node
            node=node.next
        return result

    def _is_empty():
        return self.head != None
