# given a range L-R, print XOR (L^L+1^L+2.... R-1^R)

def xor_range(l, r):
    # s = 0
    s = (1^r) ^ (1^(l-1))
    return s

a = xor_range(l=3, r = 6)
print(a)

# check if number is odd or even
def check_odd_even(n):
    if (n & 1 == 1): # for odd
        return True
    if (n & 1 == 0): # for even
        return False

b= check_odd_even(n=3)
c = check_odd_even(n=12)
print(b, c)
