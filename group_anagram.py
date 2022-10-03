def group_anagram(arr):
    hmap = {}
    for i in arr:
        c = sorted(i)
        c = "".join(c)
        if c not in hmap:
            hmap[c] = [i]
        else:
            hmap[c].append(i)
    return hmap.values()

arr = ["cat", "dog", "tac", "god", "act"]
print(group_anagram(arr))
