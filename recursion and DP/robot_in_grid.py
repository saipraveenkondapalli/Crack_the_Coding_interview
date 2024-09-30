"""
Robot in a Grid: Imagine a robot sitting in the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"
such that the robot cannot step on them.
"""


# Solution 1: Runtime O(2^(r+c)) Space O(r+c), where r is the number of rows and c is the number of columns
# This is because we are making 2 recursive calls for each cell in the grid i.e. 2^(r+c)
# The space complexity is O(r+c) because we are using a list to store the path
def robot_in_a_grid(grid):
    if not grid or not grid[0]:
        return False
    path = []
    failed_points = set()
    if get_path(grid, len(grid) - 1, len(grid[0]) - 1, path, failed_points):
        return path
    return False


def get_path(grid, row, col, path, failed_points):
    if col < 0 or row < 0 or not grid[row][col]:
        return False
    if (row, col) in failed_points: return False

    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or get_path(grid, row, col - 1, path, failed_points) or get_path(grid, row - 1, col, path,
                                                                                     failed_points):
        path.append((row, col))
        return True
    failed_points.add((row, col))
    return False


# optimized, Solution 2
def robot_in_a_grid_optimized(maze):
    if not maze or not maze[0]:
        return False
    path = []
    cache = {}
    if get_path_optimized(maze, len(maze) - 1, len(maze[0]) - 1, path, cache):
        return path
    return False


def get_path_optimized(maze, row, col, path, cache):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    p = (row, col)
    if p in cache:
        return cache[p]
    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or get_path_optimized(maze, row, col - 1, path, cache) or get_path_optimized(maze, row - 1, col,
                                                                                                 path, cache):
        path.append(p)
        cache[p] = True
        return True
    cache[p] = False
    return False


if __name__ == "__main__":
    g = [[True, True, True, True, True, False],         # - - - - - X
         [False, False, False, False, True, False],     # X X X X - X
         [True, True, True, True, True, False],         # X X X X - X
         [True, False, False, False, True, False],      # X X X X - X
         [True, True, True, True, True, True]]          # X X X X - -
    print(robot_in_a_grid(g))
    print(robot_in_a_grid_optimized(g))
