class BitSet:
    def __init__(self, size: int):
        self.bitset = [0] * ((size >> 5) + 1)

    def get(self, pos):
        word_num = pos >> 5  # divide by 32
        bit_num = pos & 0x1F  # mod 32

        return (self.bitset[word_num] & (1 << bit_num)) != 0

    def set(self, pos):
        word_num = pos >> 5
        bit_num = pos & 0x1F

        self.bitset[word_num] |= 1 << bit_num


def find_duplicates(arr: list):
    bitset = BitSet(32000)
    for num in arr:
        num0 = num - 1
        if bitset.get(num0):
            print(num)
        else:
            bitset.set(num0)

"""
Approach:
- We can use a bitset to represent the numbers from 1 to 32000.
- We can then iterate through the array and set the corresponding bit in the bitset.
- num0 = num - 1 because the bitset is 0-indexed. example: 1 is represented by 0th bit.
- If the bit is already set, we have found a duplicate.
- Time Complexity: O(n)




"""


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
    find_duplicates(arr)