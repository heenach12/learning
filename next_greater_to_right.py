def next_greater_to_right(a):
    nge = [0] * len(a)
    stack = []
    stack.append(a[len(a)-1])
    nge[(len(a)-1)] = -1
    for i in range((len(a)-2), -1,-1):
        while len(stack) > 0 and a[i] >= stack[-1]:
            stack.pop()
        if len(stack) == 0:
            nge[i] = -1
        else:
            nge[i] = stack[-1]
        stack.append(a[i])
    return nge


arr = [11, 13, 21, 3]
f = next_greater_to_right(arr)
print(f)

