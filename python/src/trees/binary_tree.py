# Created by Vasyl Paliy
# 2017

class TreeNode():
    def __init__(self, data, left=None, right=None, parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent


class BinarySearchTree():
    def __init__(self, comparator=lambda x,y: x > y):
        self.root=None
        self.comparator=comparator
        self.size=0

    # Add function using the iterative approach to prevent stack overhead
    def _add(self, data):
        node=TreeNode(data)
        if self.root:
            temp=self.root
            parent=self.root
            while temp:
                parent=temp
                # no duplicates allowed
                if temp.data == data: return
                # if the comparator returns true, then go to the left node
                temp= temp.left if self.comparator(temp.data, data) else temp.right
            node.parent=parent
            if self.comparator(parent.data, data):
                parent.left=node
            else:
                parent.right=node
        else:
            self.root=node
        self.size+=1

    def _search(self, target):
        if self.root:
            temp=self.root
            while temp:
                if temp.data == target:
                    return temp
                temp=temp.left if comparator(temp.data, target) else temp.right
        return None

    def _min(self):
        temp=self.root
        while temp and temp.left:
            temp=temp.left
        return temp

    def _max(self):
        temp=self.root
        while temp and temp.right:
            temp=temp.right
        return temp

    def _depth(self):return self.__depth__(self.root)

    def __depth__(self, node=None):
        if not node:
            return 0
        return max(self.__depth__(node.left,level)+1, self.__depth__(node.right,level)+1)

    def _mirror(self):
        if self.root:
            self.__mirror__(self.root)

    def __mirror__(self, node):
        if node:
            left=node.left
            node.left=node.right
            node.right=left
            self.__mirror__(node.right)
            self.__mirror__(node.left)

    def equals(self, tree):
        queue=[self.root, tree.root]
        while len(queue):
            first = queue.pop()
            second = queue.pop()
            if (not first) and (not second):
                if first.data != second.data:
                    return False
                queue.append(first.left)
                queue.append(second.left)
                queue.append(first.right)
                queue.append(second.right)
                if not len(queue) % 2:
                    return False
            elif not (first==None and second==None):
                return False
        return True


    def _delete(self, data):
        target=self.search(data)
        if target:
            # save the parent of the target
            parent=target.parent
            successor=None
            self.size-=1
            # if the right node is not null, then traverse to find the smallest node
            if target.right:
                successor=target.right
                # traverse the subtree to find the smallest node
                while successor.left:
                    successor=successor.left
                # modify the parent of the smallest node
                if successor.parent is not target:
                    successor.parent.left=successor.right
                    # If the successor has children, change their parent
                    if successor.right:
                        successor.right.parent=successor.parent
                successor.parent=parent
                # since the successor came from the right subtree, it should become the parent of the left
                if target.left:
                    target.left.parent=successor
            # if the right is null, then find the biggest value in the left subtree
            elif target.left:
                successor=target.left
                # Finding the greatest value
                while successor.right:
                    successor=successor.right
                # Modify the parent of the biggest value
                if successor.parent is not target:
                    successor.parent.right=successor.left
                    # If the successor has children, change their parent
                    if successor.left:
                        successor.left.parent=successor.parent
                successor.parent=parent
            if successor:
                successor.left=target.left
                successor.right=target.right
            if self.root is target:
                self.root=successor
                return
            if parent.left is target:
                parent.left=successor
            else:
                parent.right=successor


def max_node(node):
    while node and node.right:
        node=node.right
    return node

def min_node(node):
    while node and node.left:
        node=node.left
    return node

def is_bst(node):
    if node:
        max=max_node(node.left)
        min=min_node(node.right)
        not_bst=max and max.data > node.data
        not_bst=not_bst or (min and min.data < node.data)
        return not not_bst and is_bst(node.left) and is_bst(node.right)
    return True
