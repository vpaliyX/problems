
class TreeNode():
    def __init__(self, element, color, parent=None, left=None, right=None):
        self.color=color
        self.parent=parent
        self.left=left
        self.right=right


class RedBlackTree():
    def __init__(self, comparator=lambda x,y: x > y):
        self.root=None
        self.size=0

    def _add(self, element):
        if not self.root:
            self.root=TreeNode(element,color)
        else:
            node = self.root
            prev=node
            while node:
                prev=node
                node=node.left if node.element > element else node.right
            target=TreeNode(element,color=true,prev)
            if prev.element > element:
                prev.left=target
            else:
                prev.right=target
            self.size+=1

    def __balance__(self, target):
        pass
