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
            # to check if two consecutive 0s are present i.e by
            # checking if the next bit is 0(left to right) using AND operator WITH 2(10) and 'n'
            previousLength = 0 if (n & 2) == 0 else currentLength
            currentLength = 0
        maxlength = max(previousLength + currentLength + 1, maxlength)
        n = n >> 1
    return maxlength


if __name__ == "__main__":
    print(flipBitToWin(1775))  # 11011101111, answer = 8
