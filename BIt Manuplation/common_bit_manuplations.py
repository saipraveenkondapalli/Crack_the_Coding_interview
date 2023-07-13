
# get Bit

def getBit(num, i):
    return (num & (1 << i)) != 0


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    return num & ~(1 << i)


def updateBit(num, i, v):
    val = 1 if v else 0
    mask = ~(1 << i)
    return (num & mask) | (val << i)


if __name__ == "__main__":
    print(getBit(5, 2))  # 5 = 101, 1<<2 = 100 , 101 & 100 = 100, 100 != 0, True
    print(setBit(5,1))  # 5 = 101, 1<<1 = 010, 101 | 010 = 111, 7
    print(clearBit(5,2))  # 5 = 101, 1<<2 = 100, 101 & ~100 = 001, 1
    print(updateBit(5,1,1))  # 5 = 101, 1<<1 = 010, 101 & ~010 = 101, 101 | 010 = 111, 7
