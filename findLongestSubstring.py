def findLongestSubstring(a):
    n = len(a)
    st = 0
    start = 0
    maxlen=0
    last_idx = {}
    last_idx[a[0]] = 0
    for i in range(1, n):
        if a[i] not in last_idx:
            last_idx[a[i]] = i
        else:
            if last_idx[a[i]] >= st:
                curlen = i-st
                if maxlen < curlen:
                    maxlen = curlen
                    start = st
                st = last_idx[a[i]] + 1
            last_idx[a[i]] = i

    if maxlen < i-st:
        maxlen = i-st
        start = st
    return a[start: start+maxlen]

string = "abdefgabeftug"
print(findLongestSubstring(string))
