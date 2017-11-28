
# [1,2,3,4,5,6,7,9] => [9,]

class BinaryHeap():
    def __init__(self, data=None, comparator=lambda x,y:x < y):
        self.heap=data or []
        self.comparator=comparator

    def _insert(self, item):
        self.heap.append(item)
        index = len(self.heap)-1
        while index != 0:
            if self.__compare(index >> 1, index) != index:
                self.__swap(index >> 1,index)
            index=index >> 1

    def __heapify(self,index):
        left=self.__left(index)
        right=self.__right(index)
        length=len(self.heap)
        while left < length:
            final=index
            final=self.__compare(index, left)
            if right < length:
                final=self.__compare(final, right)
            if final == index:
                return
            self.__swap(final,index)
            index=final
            left=self.__left(index)
            right=self.__right(index)

    def __swap(self, first, second):
        temp=self.heap[first]
        self.heap[first]=self.heap[second]
        self.heap[second]=temp

    def __compare(self, x, y):
        return x if self.comparator(self.heap[x], self.heap[y]) else y

    def __left(self, index):
        return (index << 1) + 1

    def __right(self, index):
        return (index << 1) + 2

    def _is_empty(self):
        return index == 0
