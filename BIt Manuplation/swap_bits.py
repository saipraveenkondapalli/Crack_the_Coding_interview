"""
Swap bits :
Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g.,
bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on). EXAMPLE Input: 10101010 # 170 Output: 01010101
# 85

"""
import unittest


def swap_bits(num):
    """
    Swaps the odd and even bits in the given number
    Args:
        num:  input number

    Returns: number with odd and even bits swapped


    """
    # 0xaaaaaaaa is a 32-bit number with all even bits set as 1 and all odd bits set as 0
    # 0x55555555 is a 32-bit number with all odd bits set as 1 and all even bits set as 0

    # Example:
    # 170 = 10101010
    # 0xaaaaaaaa = 10101010101010101010101010101010
    # 0x55555555 = 01010101010101010101010101010101
    # (170 & 0xaaaaaaaa) >> 1 = 10101010 & 10101010101010101010101010101010 = 1010101
    # (170 & 0x55555555) << 1 = 10101010 & 01010101010101010101010101010101 = 101010100
    # 1010101 | 101010100 = 01010101

    return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


class Test(unittest.TestCase):
    def test_swapBits(self):
        self.assertEqual(swap_bits(170), 85)
        self.assertEqual(swap_bits(85), 170)
        self.assertEqual(swap_bits(0), 0)
        self.assertEqual(swap_bits(1), 2)
        self.assertEqual(swap_bits(2), 1)


if __name__ == "__main__":
    unittest.main()
