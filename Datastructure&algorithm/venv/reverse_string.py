def reverseString(str):
    if len(str)==1:
        return str
    else:
        return reverseString(str[1:])+str[0]
print(reverseString('yoyo mastery'))