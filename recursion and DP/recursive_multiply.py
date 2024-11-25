"""
Multipy two numbers without using * or / operator.
"""


def multipy(m, n):
    big = max(m, n)
    small = min(m, n)
    return multiply_helper1(big, small)


def multiply_helper1(big, small):
    # Runtime: O(log m) where m is the smaller number because we are dividing it by 2 each time until it reaches base
    # case
    if small == 0: return 0  # base case
    if small == 1: return big  # base case

    s = small >> 1  # divide by 2 (right shift)  Example: 5 >> 1 = 2 i.e 5(101) >> 1 = ( 1 0 )

    halfProduct = multiply_helper1(big, s)
    if small % 2 == 0:  # even
        return halfProduct + halfProduct  # double it
    else:
        return halfProduct + halfProduct + big  # double it and add the big number to it


# memiozation solution

def multiply_helper2(big, small, memo=[]):
    if small == 0:
        return 0
    elif small == 1:
        return big

    elif memo[small] > 0:
        return memo[small]

    small >>= 1  # divide by 2

    half_product = multiply_helper2(big, small, memo)

    if small % 2 == 0:  # small is even
        memo[small] = half_product + half_product
    else:
        memo[small] = half_product + half_product + big

    return memo[small]


# optimized solution
def multiply2(a, b):
    result = 0
    a, b = max(a, b), min(a, b)
    while b:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result


if __name__ == "__main__":
    print(multipy(31, 35))  # 1085
    print(multiply2(31, 35))  # 1085
