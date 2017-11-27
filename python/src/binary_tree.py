# Created by Vasyl Paliy
# 2017

class TreeNode():
    def __init__(self, data, left=None, right=None, parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent


class BinaryTree():
    def __init__(self, comparator=lambda x,y: x > y):
        self.root=None
        self.comparator=comparator
        self.size=0

    # Add function using the iterative approach to prevent stack overhead
    def _add(self, data):
        node=TreeNode(data)
        if self.root != None:
            temp=self.root
            parent=self.root
            while temp!=None:
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
        if self.root!=None:
            temp=self.root
            while temp!=None:
                if temp.data == target:
                    return temp
                temp=temp.left if comparator(temp.data, target) else temp.right
        return None

    def _min(self):
        temp=self.root
        while temp !=None and temp.left!=None:
            temp=temp.left
        return temp

    def _max(self):
        temp=self.root
        while temp!=None and temp.right!=None:
            temp=temp.right
        return temp

    def _depth(self):return self.__depth__(self.root)

    def __depth__(self, node=None):
        if node == None:
            return 0
        return max(self.__depth__(node.left,level)+1, self.__depth__(node.right,level)+1)

    def _mirror(self):
        if self.root != None:
            self.__mirror__(self.root)

    def __mirror__(self, node):
        if node != None:
            left=node.left
            node.left=node.right
            node.right=left
            self.__mirror__(node.right)
            self.__mirror__(node.left)

    def _delete(self, data):
        target=self.search(data)
        if target != None:
            # save the parent of the target
            parent=target.parent
            successor=None
            self.size-=1
            # if the right node is not null, then traverse to find the smallest node
            if target.right!=None:
                successor=target.right
                # traverse the subtree to find the smallest node
                while successor.left !=None:
                    successor=successor.left
                # modify the parent of the smallest node
                if successor.parent is not target:
                    successor.parent.left=successor.right
                    # If the successor has children, change their parent
                    if successor.right!=None:
                        successor.right.parent=successor.parent
                successor.parent=parent
                # since the successor came from the right subtree, it should become the parent of the left
                if target.left!=None:
                    target.left.parent=successor
            # if the right is null, then find the biggest value in the left subtree
            elif target.left!=None:
                successor=target.left
                # Finding the greatest value
                while successor.right!=None:
                    successor=successor.right
                # Modify the parent of the biggest value
                if successor.parent is not target:
                    successor.parent.right=successor.left
                    # If the successor has children, change their parent
                    if successor.left!=None:
                        successor.left.parent=successor.parent
                successor.parent=parent
            if successor!=None:
                successor.left=target.left
                successor.right=target.right
            if self.root is target:
                self.root=successor
                return
            if parent.left is target:
                parent.left=successor
            else:
                parent.right=successor
