def Substr(s1, s2):
    counter = 0
    i = 0
    n = len(s1)
    while(i < n):
        if counter == len(s2):
            break
        if s2[counter] == s1[i]:
            counter += 1
        else:
            if counter > 0:
                i =i-counter
            counter = 0
        i += 1
    if counter< len(s2):
        return -1
    else:
        return  (i-counter)
    #
    #
    #
    # counter = 0
    # i = 0
    # Len = len(s1)
    #
    # while (i < Len):
    #     if (counter == len(s2)):
    #         break;
    #     if (s2[counter] == s1[i]):
    #         counter += 1
    #     else:
    #         if (counter > 0):
    #             i -= counter
    #         counter = 0
    #     i += 1
    #
    # if (counter < len(s2)):
    #     return -1
    # else:
    #     return (i - counter)


# Driver code
print(Substr("geeksforgeeks", "for"))
