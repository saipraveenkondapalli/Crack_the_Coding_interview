
# get Bit

def get_bit(num, i):
    return (num & (1 << i)) != 0


def set_bit(num, i):
    return num | (1 << i)


def clear_bit(num, i):
    return num & ~(1 << i)


def update_bit(num, i, v):
    val = 1 if v else 0
    mask = ~(1 << i)
    return (num & mask) | (val << i)


if __name__ == "__main__":
    print(get_bit(5, 2))  # 5 = 101, 1<<2 = 100 , 101 & 100 = 100, 100 != 0, True
    print(set_bit(5, 1))  # 5 = 101, 1<<1 = 010, 101 | 010 = 111, 7
    print(clear_bit(5, 2))  # 5 = 101, 1<<2 = 100, 101 & ~100 = 001, 1
    print(update_bit(5, 1, 1))  # 5 = 101, 1<<1 = 010, 101 & ~010 = 101, 101 | 010 = 111, 7
