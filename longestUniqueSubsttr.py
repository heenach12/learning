def longestUniqueSubsttr(string):
    string_dict = {}
    start_idx = 0
    max_len = 0
    for i in range(0, len(string)):
        if string[i] in string_dict:
            start_idx = max(start_idx, string_dict[string[i]]+1)
        max_len = max(max_len, i-start_idx+1)
        string_dict[string[i]] = i
    return max_len


    # last_idx = {}
    # start_idx = 0
    # max_len = 0
    # for i in range(len(string)):
    #     if string[i] in last_idx:
    #         start_idx = max(start_idx, last_idx[string[i]]+1)
    #     max_len = max(max_len, i-start_idx+1)
    #     last_idx[string[i]] = i
    # return max_len

    # sliding window approach
    # max_len = 0
    # for i in range(len(string)):
    #     visited = [0] * 256
    #     for j in range(i, len(string)):
    #         if visited[ord(string[j])] == True:
    #             break
    #         else:
    #             max_len = max(max_len, j-i+1)
    #             visited[ord(string[j])] = True
    #     visited[ord(string[i])] = False
    # return max_len

# Driver program to test the above function
string = "abdefgabefty"
print(longestUniqueSubsttr(string))
