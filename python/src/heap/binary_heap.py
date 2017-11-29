# Created By Vasyl Paliy
# 2017

class BinaryHeap():
    def __init__(self, container=None, comparator=lambda x,y: x < y):
        self.container=container or []
        self.comparator=comparator
        for index in xrange(len(self.container) / 2 -1, -1, -1):
            self.__down(index)

    def insert(self, item):
        self.container.append(item)
        index = len(self.container)-1
        while index > 0:
            parent = self.__parent(index)
            if self.comparator(self.container[parent], self.container[index]):
                self.__swap(parent, index)
                index = parent
                continue
            return

    def __swap(self, x, y):
        temp=self.container[x]
        self.container[x]=self.container[y]
        self.container[y]=temp

    def __left(self, index):
        return (index << 1) + 1

    def __right(self, index):
        return (index << 1) + 2

    def __parent(self, index):
        return index >> 1 if (index % 2) else (index >> 1) -1

    def __compare(self, x, y):
        if x < self.size() and y < self.size():
            return y if self.comparator(self.container[x], self.container[y]) else x
        return x

    def top(self):
        result = self.container[0]
        self.__swap(0,self.size()-1)
        self.container=self.container[:-1]
        self.__down(0)
        return result

    def __down(self, index):
        while True:
            left = self.__left(index)
            right = self.__right(index)
            result = self.__compare(index, left)
            result = self.__compare(result, right)
            if result == index:
                return
            self.__swap(result, index)
            index = result

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0
