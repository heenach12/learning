def selection_sort(a, n):
    for i in range(0, n):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j

        a[min_idx], a[i] = a[i], a[min_idx]
    return a

arr = [64, 34, 25, 12, 22, 11, 90]

for i in arr:
    print(i, id(i), end=" ")

selection_sort(arr, len(arr))
print("**********")

for i in arr:
    print(i, id(i), end=" ")



open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check(string))

string = "[{}{})(]"
print(string, "-", check(string))

string = "((()"
print(string, "-", check(string))
