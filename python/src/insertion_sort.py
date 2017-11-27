def insertionSort(array, comparator=lambda x,y: x > y):
    if array!=None:
        for index in xrange(0,len(array)-1):
            key=array[index+1]
            jIndex=index+1
            while jIndex !=0 and not comparator(array[jIndex-1],key):
                array[jIndex]=array[jIndex-1]
                jIndex-=1
            array[jIndex]=key
