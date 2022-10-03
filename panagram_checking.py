def panagram_checking(s):

    l = []
    for i in range(26):
        l.append(False)

    for i in s.lower():
        if not i == " ":
            l[ord(i)-ord('a')] = True

    for ch in l:
        if ch == False:
            return False
    return True


sentence = "The quick brown fox jumps over the little lazy dog"

if (panagram_checking(sentence)):
    print("is a pangram")
else:
    print("is not a pangram")
