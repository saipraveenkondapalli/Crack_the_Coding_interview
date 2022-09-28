from common_bit_manuplations import getBit, setBit, clearBit, updateBit


def insertBits(m,n, i, j):
    # clear bits from i to j in n
    for k in range(i,j+1):
        n = clearBit(n,k)
    # shift m by i bits
    m = m << i
    print(bin(m))
    # merge m and n
    return n | m



if __name__ == "__main__":
    N = 1024
    M = 19
    i = 2
    j = 6

    print("M: ", bin(M))
    print("N: ", bin(N))
    if j-i+1 < len(bin(M)[2:]):
        print("N can't be inserted in M")
    else:

        print("Result: ", bin(insertBits(M,N,i,j)))