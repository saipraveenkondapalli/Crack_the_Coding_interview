"""
Multipy two numbers without using * or / operator.
"""


def multipy2(m, n):
    big = max(m, n)
    small = min(m, n)
    return multiply_helper2(big, small)


def multiply_helper2(big, small):
    # Runtime: O(log m) where m is the smaller number because we are dividing it by 2 each time until it reaches base case
    if small == 0: return 0 # base case
    if small == 1: return big # base case
    s = small >> 1  # divide by 2 (right shift)  Example: 5 >> 1 = 2 i.e 5(101) >> 1 = ( 1 0 )
    halfProduct = multiply_helper2(big, s)
    if small % 2 == 0:  # even
        return halfProduct + halfProduct  # double it
    else:
        return halfProduct + halfProduct + big  # double it and add the big number to it


if __name__ == "__main__":
    print(multipy2(31,35)) # 1085


