"""
Given a binary string, count number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”
"""
def count_substrings(st):
    # res = 0
    n= len(st)
    # for i in range(0, len(st)):
    #     if st[i] == "1":
    #         for j in range(i+1, n):
    #             if st[j] == "1":
    #                 res += 1
    # return res

    m = 0
    for i in range(0, n):
        if st[i] == "1":
            m += 1
    return m*(m-1)//2


st = "00100101"
print(count_substrings(st))
