"""
Problem: Search in a Sorted Matrix
Given an M x N matrix in which each row and each column is sorted in ascending order, write a method to find an element.

"""


def search_in_sorted_matrix(mat: list, target: int) -> tuple:
    if not mat:
        return -1, -1

    rows = len(mat)
    cols = len(mat[0])

    row = 0
    col = cols - 1

    while row < rows and col >= 0:
        current = mat[row][col]

        if current == target:
            return row, col
        elif current < target:
            row += 1
        else:
            col -= 1

    return -1, -1


if __name__ == "__main__":
    m = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
    print(search_in_sorted_matrix(m, 10))  # (2, 1)
