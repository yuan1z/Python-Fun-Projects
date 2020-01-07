def mergeSortedArray(arr1,arr2):
    arr = []
    i,j = 0,0
    while i < len(arr1):
        if arr2[j]> arr1[i]:
            arr.append(arr1[i])
            i+=1
        elif j == len(arr2)-1:
            arr.append(arr1[i])
            i+=1
        elif arr2[j]<=arr1[i]:
            arr.append(arr2[j])
            j+=1
    while j< len(arr2):
        arr.append(arr2[j])
        j+=1


    return arr
if __name__ == "__main__":
    arr1 = [0,3,4,31]
    arr2 = [4,6,30,32,33]
    print(mergeSortedArray(arr1,arr2))


