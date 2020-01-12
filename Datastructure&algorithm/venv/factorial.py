def findFactorialRecursice(number):
    if number == 0:
        return 1
    else:
        return findFactorialRecursice(number-1)*number
def findFactorialIterative(number):
    tmp = 1
    for i in range(1,number+1):
        tmp*=i
    return tmp
print(findFactorialRecursice(5))
print(findFactorialIterative(5))