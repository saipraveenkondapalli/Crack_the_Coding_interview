"""Rotate Matrix
Given an image represented by 90 degrees, write a method to rotate the image by 90 degrees. Can you do this in place?"""

import unittest

# book solution 1
def rotatematrix(mat):
    # Runtime O(n^2) Space O(n^2) since any algorithm must touch every element in the matrix i.e n*n
    if len(mat) != len(mat[0]):
        return False
    n = len(mat)
    for layer in range(n//2):
        first = layer
        last  = n-1-layer
        for i in range(first, last):
            offset = i-first
            top = mat[first][i]

            # move left to top 
            mat[first][i] = mat[last-offset][first]

            # move bottom to left 
            mat[last-offset][first] = mat[last][last-offset]

            # move right to bottom 
            mat[last][last-offset] = mat[i][last]

            # move top to right 
            mat[i][last] = top
    return mat



class Test(unittest.TestCase):
    data = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]),
        ([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]],
         [[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]),
        ([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36]],
         [[31,25,19,13,7,1],[32,26,20,14,8,2],[33,27,21,15,9,3],[34,28,22,16,10,4],[35,29,23,17,11,5],[36,30,24,18,12,6]])

    ]

    def test_rotatematrix(self):
        for [mat, expected] in self.data:
            actual = rotatematrix(mat)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()


