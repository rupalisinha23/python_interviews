import math


def reverse(x: int) -> int:
    # y = str(x)
    # return int(float(y[::-1]))
    rev = 0
    neg = False
    if x < 0:
        neg = True
    if neg:
        x = -x
    while x != 0:
        rem = x % 10
        rev = rev*10 + rem
        x = int(x/10)
    if rev >= math.pow(2, 31) - 1 or -rev < -math.pow(2, 31):
        return 0
    if neg:
        return -rev
    return rev


print(reverse(1563847412))