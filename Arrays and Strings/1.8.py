# zero matrix 

from contextlib import nullcontext
from pickle import TRUE
import unittest


# book solution 1

def zeromatrix(mat):

    # space O(m*n)
    r, c = len(mat), len(mat[0])
    row = [False for _ in range(r)]
    col = [False for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                row[i] = True
                col[j] = True
    
    # set rows to zero
    for i in range(r):
        if row[i]:
            for j in range(c):
                mat[i][j] = 0
    # set cols to zero
    for j in range(c):
        if col[j]:
            for i in range(r):
                mat[i][j] = 0
    return mat


#------------------------------ wrapper functions ----------------------------------------------
def nullifyRow(mat, i):
    r,c = len(mat), len(mat[0])
    for j in range(c):
        mat[i][j] = 0

def nullifyCol(mat,j):
    r,c= len(mat), len(mat[0])
    for i in range(r):
        mat[i][j] = 0

# ------------------------- End of Wrapper Functions----------------------------------

# book solution 2
"""
Hold the code for review, code is not working, look for bugs and fix later

"""
def zeromatrix2(mat):
    rowHasZero = False
    colHasZero = False
    # check if first row has a zero 
    r,c= len(mat), len(mat[0])
    for j in range(r):
        if mat[0][j] == 0:
            rowHasZero = True
    #check if first col has a zero 
    for i in range(r):
        if mat[i][0] == 0:
            colHasZero = True

    # check for zeros in rest of the array
    for i in range(1,r):
        for j in range(1,c):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0
    # Nulllify rows based in values in first column
    for i in range(r):
        if mat[i][0] == 0:
            nullifyRow(mat, 0)

    # nullify col based on values in first row
    for j in range(c):
        if mat[j][0] == 0:
            nullifyCol(mat, j)

    if rowHasZero:
        nullifyRow(mat,0)
    if colHasZero:
        nullifyCol(mat,0)

    return mat

class Test(unittest.TestCase):
    data = [
        (
            [
                [1,2,3],
                [4,0,6],
                [7,8,9]
            ],
            [
                [1,0,3],
                [0,0,0],
                [7,0,9]
            ]
        ),
        (
            [
                [1,2,3,4],
                [5,0,7,8],
                [9,10,11,12],
                [13,14,15,16]
            ],
            [
                [1,0,3,4],
                [0,0,0,0],
                [9,0,11,12],
                [13,0,15,16]
            ]
        )

    ]



    def test_zero_matrix(self):
        for test_mat, expected in self.data:
            actual = zeromatrix2(test_mat)
            self.assertEqual(actual, expected)




if __name__ == "__main__":
    
    unittest.main()

