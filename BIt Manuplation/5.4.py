"""

Next Number:
Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
Example:
Input: 13948 (or: 1101 0100 1100 0100)
Output: 13971, 13967 # 1101 0100 1110 0011, 1101 0100 1100 0111

"""

def nextLargest(n):
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
    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n # returns the next largest number with the same number of 1 bits


def nextSmallest(n):
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
    p = c0 + c1
    n &= ((~0) << (p + 1))
    print(n)
    mask = (1 << (c1 + 1)) - 1
    print(mask)
    n |= mask << (c0 - 1)
    return n   # returns the next smallest number with the same number of 1 bits


def nextSmallestAndLargest(n):
    return [nextSmallest(n), nextLargest(n)]


if __name__ == "__main__":
   # print(nextSmallestAndLargest(13948))
    #print(nextSmallestAndLargest(13967))
    #print(nextSmallestAndLargest(0))
    print(nextSmallestAndLargest(6))
   