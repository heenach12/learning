def getMax(operations):
    print(operations)
    stack = []
    for i in range(len(operations)):
        q = operations[i].split()
        # print("q is", q)
        if q[0] == "1":
            if stack:
                stack.append(max(stack[len(stack) - 1], q[1]))
            else:
                stack.append(q[1])
        elif q[0] == "2":
            stack.pop()
        else:
            print(stack[len(stack) - 1])

operations = ['1 97', '2', '1 20', '2', '1 26', '1 20', '2', '3', '1 91', '3']
res = getMax(operations)
print("the result is ", res)

