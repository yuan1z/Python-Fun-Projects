def find(arr):
    mydict = {}
    for item in arr:
        if item in mydict:
            mydict[item]+=1
        else:
            mydict[item] = 1
        if mydict[item] == 2:
            return item
    return None

print(find([2,5,1,2,3,5,1,2,4]))
print(find([2,1,1,2,3,4,1,2,4]))
print(find([2,3,4,5]))