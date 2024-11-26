"""
Queen: Write an algorithm to print all ways of arranging eight queens on an 8x8
chess board so that none of them share the same row, column or diagonal.
In this case, "diagonal" means all diagonals, not just the two that bisect the board.
"""


def place_queens(row, columns, results):
    if row == 8:
        results.append(columns[:])
    else:
        for col in range(8):
            if check_valid(columns, row, col):
                columns[row] = col
                place_queens(row + 1, columns, results)


def check_valid(columns, row1, column1):
    for row2 in range(row1):  # check each row
        column2 = columns[row2]  # get column of row2
        if column1 == column2:  # check column is same as column2
            return False
        column_distance = abs(column2 - column1)  # check diagonal is same as column2
        row_distance = row1 - row2
        if column_distance == row_distance:
            return False
    return True


if __name__ == "__main__":
    r = []
    c = [0] * 8
    place_queens(0, c, r)
    print(*r, sep="\n")
    print(len(r))
