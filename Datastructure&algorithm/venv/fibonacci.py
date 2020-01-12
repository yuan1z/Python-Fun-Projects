def fibonaciiIterative(n):
    a,b = 0,1
    i = 2
    while i <= n:
        tmp = a+b
        a = b
        b = tmp
        i+=1
    return tmp

def fibonaciiRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaciiRecursive(n-1)+fibonaciiRecursive(n-2)


print(fibonaciiIterative(6))
print(fibonaciiRecursive(6))