def fibonaciiIterative(n):
    a,b = 0,1
    i = 2
    while i <= n:
        tmp = a+b
        a = b
        b = tmp
        i+=1
    return tmp

def fibonaciiRecursive(n): #O(2^n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaciiRecursive(n-1)+fibonaciiRecursive(n-2)

def fibonaciiDP(n,cache): #O(n)
    if n == 0 :
       return 0
    elif n == 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fibonaciiDP(n-1,cache)+fibonaciiDP(n-2,cache)
        return cache[n]

print(fibonaciiIterative(6))
print(fibonaciiRecursive(6))
print(fibonaciiDP(6,{}))