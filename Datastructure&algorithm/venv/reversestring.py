def reverse(string):
    my_list = list(string)
    print(my_list)
    res = []
    i = len(string)-1
    while i >= 0:
        res.append(my_list[i])
        i-=1
    return ''.join(res)

if __name__ == "__main__":
    string1 = 'Hi My name is Andrei'
    print(reverse(string1))