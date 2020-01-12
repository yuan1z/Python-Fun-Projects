def selectionSort(arr):
    j = 0
    while j < len(arr):
        i = j
        min_idx = j
        while i < len(arr):
            if arr[i]< arr[min_idx]:
                min_idx = i
            i+=1
        tmp = arr[j]
        arr[j] = arr[min_idx]
        arr[min_idx] = tmp
        print(arr)
        j+=1

numbers = [99,44,6,2,1,5,63,87,283,4,0]
selectionSort(numbers)
print(numbers)