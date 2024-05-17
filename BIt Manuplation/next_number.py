"""

5.4 Next Number:
Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bit in their binary representation.
Example:
Input: 13948 (or: 1101 0100 1100 0100)
Output: 13971, 13967 # 1101 0100 1110 0011, 1101 0100 1100 0111

"""


def next_largest(n):
    c = n
    c0 = 0
    c1 = 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    p = c0 + c1
    n |= (1 << p)  # flip the rightmost non-trailing zero
    n &= ~((1 << p) - 1)  # clear all bits to the right of p
    n |= (1 << (c1 - 1)) - 1  # insert (c1-1) ones on the right
    return n  # returns the next largest number with the same number of 1s


def next_smallest(n):
    temp = n
    c0 = 0
    c1 = 0
    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1
    if temp == 0:
        return -1
    while (temp & 1) == 0 and temp != 0:
        c0 += 1
        temp >>= 1
    p = c0 + c1  # position of rightmost non-trailing one
    n &= ((~0) << (p + 1))  # clears from bit p onwards

    mask = (1 << (c1 + 1)) - 1  # sequence of (c1+1) ones right aligned to p

    n |= mask << (c0 - 1)  # c0-1 zeros on the right
    return n  # returns the next smallest number with the same number of 1 bits


def next_smallest_and_largest(n):
    return [next_smallest(n), next_largest(n)]


if __name__ == "__main__":
    print(next_smallest_and_largest(10))
