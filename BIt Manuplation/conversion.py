"""
5.6 Conversion :
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

"""


def bit_swap_required(a, b):
    count = 0
    c = a ^ b
    while c:
        count += c & 1
        c >>= 1
    return count


if __name__ == "__main__":
    print(bit_swap_required(29, 15))  # 2
    print(bit_swap_required(29, 0))  # 4
    print(bit_swap_required(0, 0))  # 0
