"""

Flip a bit to win

"""


def flipBitToWin(n):
    if ~n == 0:
        return len(bin(n)[2:])
    currentLength = 0
    previousLength = 0
    maxlength = 1
    while n != 0:
        if n & 1 == 1:
            currentLength += 1
        elif n & 1 == 0:
            previousLength = 0 if (n & 2) == 0 else currentLength
            currentLength = 0
       # print(currentLength, previousLength, maxlength)
        maxlength = max(previousLength+currentLength+1, maxlength)
        n = n >> 1
    return maxlength



if __name__ == "__main__":
    print(flipBitToWin(1775)) # 11011101111, answer = 8
    #print(flipBitToWin(0b1111111111111111111111111111111)) # 31
