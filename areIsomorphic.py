def areIsomorphic(str1, str2):
    hmap = dict()
    c = "a"
    l = len(str1)
    for i in range(l):
        if str1[i] in hmap:
            c = hmap[str1[i]]
            if c != str2[i]:
                return False
        elif str2 not in hmap.values():
            hmap[str1[i]] = str2[i]
        else:
            return False
    return True


# Driver Code
str1 = "aac"
str2 = "xxy"

# Function Call
if (len(str1) == len(str2) and areIsomorphic(str1, str2)):
    print(1)
else:
    print(0)
