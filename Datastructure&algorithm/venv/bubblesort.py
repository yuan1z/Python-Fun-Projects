def bubbleSort(array):
    length = len(array)
    while length > 0:
        i = 0
        while i < length-1:
            if array[i]> array[i+1]:
                tmp = array[i+1]
                array[i+1]= array[i]
                array[i] = tmp
            else:
                pass
            i+=1
        length-=1
numbers = [99,44,6,2,1,5,63,87,283,4,0]
bubbleSort(numbers)
print(numbers)

