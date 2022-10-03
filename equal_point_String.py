def findIndex(str):
    cnt_close = 0
    l = len(str)
    for i in range(1, l):
        if (str[i] == ')'):
            cnt_close = cnt_close + 1

    for i in range(1, l):
        if (cnt_close == i):
            return i
    # If no opening brackets
    return l


# Driver Code
str = "(()))(()()())))"
print(findIndex(str))
