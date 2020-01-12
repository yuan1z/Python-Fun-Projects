def insertionSort(arr):
    i = 0
    while i < len(arr):
        j = 0
        while j < i:
            if arr[i] < arr[j]:
                x = arr.pop(i)
                arr.insert(j,x)
            j+=1
        i+=1

numbers = [99,44,6,2,1,5,63,87,283,4,0]
insertionSort(numbers)
print(numbers)