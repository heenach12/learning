def swap_numbers(a, b):
    a=a^b
    b=a^b
    a=a^b
    return a, b


a, b = swap_numbers(a=5, b=2)
print(a, b)
