def if_ith_bit_set(i, n):
    mask = 1 << i  # this gives the mask of the number at the ith bit

    d = mask & n
    if d:
        return True
    else:
        return False

d =if_ith_bit_set(i=3, n=17)
print("d i", d)
