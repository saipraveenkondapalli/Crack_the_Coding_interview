"""
5.3
Flip a bit to win: You have an integer, and you can flip exactly one bit from a 0 to a 1. Write code to find the length
of the longest sequence of 1s you could create.
EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8

"""


def flip_bit_to_win(n):
    if ~n == 0:
        return len(bin(n)[2:])
    current_length = 0
    previous_length = 0
    max_length = 1
    while n != 0:
        if n & 1 == 1:
            current_length += 1
        elif n & 1 == 0:
            # to check if two consecutive 0s are present i.e by
            # checking if the next bit is 0(left to right) using AND operator WITH 2(10) and 'n'
            previous_length = 0 if (n & 2) == 0 else current_length
            current_length = 0
        max_length = max(previous_length + current_length + 1, max_length)
        n = n >> 1
    return max_length


if __name__ == "__main__":
    print(flip_bit_to_win(1775))  # 11011101111, answer = 8
