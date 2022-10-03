def xor_numbers(n):
    s = 0
    if (n%4 == 0):
        s=n
    if (n%4 == 1):
        s= 1
    if (n%4==2):
        s=n+1
    if (n%4==3):
        s=0
    return s


n = 5
d = xor_numbers(n=5)
print(d)
