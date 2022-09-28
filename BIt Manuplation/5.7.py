"""
Swap bits : Write a program to swap odd and even bits in an integer with as few instructions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
EXAMPLE
Input: 10101010 # 170
Output: 01010101 # 85

"""
import unittest


def swapBits(num):
    return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


class Test(unittest.TestCase):
    def test_swapBits(self):
        self.assertEqual(swapBits(170), 85)
        self.assertEqual(swapBits(85), 170)
        self.assertEqual(swapBits(0), 0)
        self.assertEqual(swapBits(1), 2)
        self.assertEqual(swapBits(2), 1)


if __name__ == "__main__":
    unittest.main()
