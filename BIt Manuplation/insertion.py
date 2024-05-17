from common_bit_manuplations import clear_bit

"""
5.1 insertion:
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M 
into N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to 
fit all of M. That is, if M = 10011, you can assume that there are at least 5 bits between j and i. You would not, 
for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2. 
EXAMPLE 
Input: N = 10000000000, M = 10011, i = 2, j = 6 Output: N = 10001001100
"""


def insert_bits(m, n, i, j):
    # clear bits from i to j in n
    for k in range(i, j + 1):
        n = clear_bit(n, k)
    # shift m by i bits
    m = m << i

    # merge m and n
    return n | m


# without using clearBit

def insert_bits2(m, n, i, j):
    #  clear bits from i to j in N by creating a mask. example N = 10000000000, i = 2, j = 6, M = 10011
    all_ones = ~0
    # shift allOnes by j+1 bits
    left = all_ones << (j + 1)  # 11100000000
    # shift 1 by i bit
    right = (1 << i) - 1  # 00000000011

    # create mask by ORing left and right
    mask = left | right  # 11100000011 i.e bits from i to j are 0 and rest are 1
    # clear bits from i to j in N
    n = n & mask  # 10000000000 & 11100000011 = 10000000000
    # shift m by i bits
    m = m << i  # 10011000000 i.e to insert m in n, we need to shift m by i bits to align it with i in n
    # merge m and n
    return n | m


if __name__ == "__main__":
    N = 10245
    M = 19
    i = 2
    j = 6

    print("M:      ", bin(M)[2:], "(", M, ")")
    print("N:      ", bin(N)[2:], "(", N, ")")
    if j - i + 1 < len(bin(M)[2:]):
        print("N can't be inserted in M")
    else:

        print("Result: ", bin(insert_bits2(M, N, i, j))[2:], "(", insert_bits2(M, N, i, j), ")")
