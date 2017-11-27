def merge(array, left, right, comparator):
    middle=(left+right)/2 -1
    leftSize=middle-left+1
    rightSize=right-middle-1
    leftArray, rightArray=[0]*leftSize,[0]*rightSize
    for index in xrange(leftSize):
        leftArray[index]=array[left+index]
    for index in xrange(rightSize):
        rightArray[index]=array[middle+index+1]
    leftIndex,rightIndex=0,0
    def mergeLast(subArray, index):
        for element in subArray:
            array[index]=element
            index+=1
    while True:
        if comparator(leftArray[leftIndex], rightArray[rightIndex]):
            array[left]=leftArray[leftIndex]
            leftIndex+=1
            if leftIndex == leftSize:
                mergeLast(rightArray[rightIndex:],left+1)
                return
        else:
            array[left]=rightArray[rightIndex]
            rightIndex+=1
            if rightIndex == rightSize:
                mergeLast(leftArray[leftIndex:],left+1)
                return
        left+=1

def mergeSort(array, left, right, comparator=lambda x,y:x > y):
    if left < right-1:
        middle = (left+right)/2 -1
        mergeSort(array,left,middle+1,comparator)
        mergeSort(array,middle+1,right,comparator)
        merge(array, left, right,comparator)
