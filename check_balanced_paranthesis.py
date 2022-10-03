open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def check_balanced(input_str):
    s = []
    for i in input_str:
        if i in open_list:
            s.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(s) > 0 and open_list[pos] == s[len(s)-1]:
                s.pop()
            else:
                return "Unbalanced"
    if len(s) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


string = "{[]{()}}"
print(check_balanced(input_str=string))
string = "[{}{})(]"
print(check_balanced(input_str=string))
