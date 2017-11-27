class Node():
    def __init__(self,data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    # add a node to the end of the list O(1)
    def _add_end(self, data):
        target=Node(data)
        self.length+=1
        if self.head != None:
            target.prev=self.tail
            self.tail=self.tail.next=target
        else:
            self.head=self.tail=target

    # add a node to the front O(1)
    def _add_front(self, data):
        target=None(data)
        self.length+=1
        if self.head != None:
            target.next=self.head
            self.head=target.next.prev=target
        else:
            self.head=self.tail=target

    # remove a node by its value O(n)
    def _remove_value(self, value):
        temp=self.head
        while temp != None:
            if temp.data == value:
                self.__remove_node(temp)
                return
            temp=temp.next

    # private method to remove a node O(1)
    def __remove_node(self, node):
        self.length-=1
        # if the node has next, then link the next node with the previous
        if node.next != None:
            node.next.prev=node.prev
        # if the node has previous, then link the previous node with the next
        if node.prev !=None:
            node.prev.next=node.next
        # in case if the node is the head node, change the head
        if node is self.head:
            self.head=self.head.next
            # if it was the only node, then invalidate
            if self.head == None:
                self.tail=None
                del node
                return
            self.head.prev=None
        # shift the tail node if necessary
        if node is self.tail:
            self.tail=self.tail.prev
            self.tail.next=None
        del node

    # removes a node by its position in the list O(n)
    # slightly optimized, so you don't have to traverse through the entire list
    def _remove_at(self, index):
        if index < self.length:
            node=None
            index=self.length-index
            if index < self.length / 2:
                node = self.tail
                while index >= 1:
                    node=node.prev
                    index-=1
            else:
                node = self.head
                while index > 0:
                    node=node.next
                    index-=1
            self.__remove_node(node)

    # reverses the list O(n)
    def _reverse(self):
        node=self.head
        self.head=self.tail
        self.tail=node
        prev=node.prev
        while node != None:
            next=node.next
            node.next=prev
            node.prev=next
            prev=node
            node=next

    # returns true if the value is in the list O(n)
    def _contains(self, key):
        temp=self.head
        while temp != None:
            if temp.data == key:
                return True
            temp=temp.next
        return False
