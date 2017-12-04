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

    def delete_node(self, key):
        target=self.search(key)
        if self.root is target:
            del self.root
        elif target:
            successor=None
            parent=target.parent
            self.size-=1
            # if true, then extract the very left child of the right subtree
            if target.left and target.right:
                successor=target.right
                # navigate to the left tree
                while successor.left:
                    successor=successor.left
                # if the successor is not the right node of the target
                if successor.parent is not target:
                    successor.parent.left=successor.right
                    if successor.right:
                        successor.right.parent=successor.parent
            elif target.left or target.right:
                successor=target.left if target.left else target.right
            if parent:
                if parent.left is target:
                    parent.left=successor
                else:
                    parent.right=successor
            if successor:
                successor.parent=parent
                
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
