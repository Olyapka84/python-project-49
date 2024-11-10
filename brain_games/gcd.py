def evklid(a, b):
    while b != 0:
        a, b = b, b % a
    return a