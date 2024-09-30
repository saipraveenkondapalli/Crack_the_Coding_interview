"""
Robot in a Grid: Imagine a robot sitting in the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"
such that the robot cannot step on them.
"""


# Solution 1: This solution uses recursion and memoization with a set to keep track of failed points. The runtime
# complexity is O(2^(r+c)) and the space complexity is O(r+c), where r is the number of rows and c is the number of
# columns.

def robot_in_a_grid(grid):
    """
    This function finds a path for the robot in the grid.

    :param grid: 2D list representing the grid
    :return: List of tuples representing the path if one exists, False otherwise
    """
    if not grid or not grid[0]:
        return False
    path = []
    failed_points = set()
    if get_path(grid, len(grid) - 1, len(grid[0]) - 1, path, failed_points):
        return path
    return False


def get_path(grid, row, col, path, failed_points):
    """
    This helper function uses recursion to find a path.

    :param grid: 2D list representing the grid
    :param row: Current row
    :param col: Current column
    :param path: List to store the path
    :param failed_points: Set to store the points where a path could not be found
    :return: True if a path is found, False otherwise
    """
    if col < 0 or row < 0 or not grid[row][col]:
        return False

    if (row, col) in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)  # base case , we are at the origin

    # if we are at the origin, or we can reach the origin from the current cell
    if is_at_origin or get_path(grid, row, col - 1, path, failed_points) or get_path(grid, row - 1, col, path,
                                                                                     failed_points):
        path.append((row, col))
        return True

    # if we can't reach the origin from the current cell, we add the cell to the failed points
    failed_points.add((row, col))
    return False


# Optimized Solution 2: This solution also uses recursion, but with a dictionary for memoization.
def robot_in_a_grid_optimized(maze):
    """
    This function finds a path for the robot in the maze.

    :param maze: 2D list representing the maze
    :return: List of tuples representing the path if one exists, False otherwise
    """
    if not maze or not maze[0]:
        return False
    path = []
    cache = {}
    if get_path_optimized(maze, len(maze) - 1, len(maze[0]) - 1, path, cache):
        return path
    return False


def get_path_optimized(maze, row, col, path, cache):
    """
    This helper function uses recursion to find a path and memoizes the results.

    :param maze: 2D list representing the maze
    :param row: Current row
    :param col: Current column
    :param path: List to store the path
    :param cache: Dictionary to store the results of previous computations
    :return: True if a path is found, False otherwise
    """
    if col < 0 or row < 0 or not maze[row][col]:  # if we are out of bounds, or we hit a wall
        return False

    p = (row, col)
    if p in cache:  # if we have already visited this cell
        return cache[p]

    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or get_path_optimized(maze, row, col - 1, path, cache) or get_path_optimized(maze, row - 1, col,
                                                                                                 path, cache):
        path.append(p)
        cache[p] = True  # if we can reach the origin from the current cell, we add the cell to the cache
        return True

    cache[p] = False  # if we can't reach the origin from the current cell, we add the cell to the cache

    return False


if __name__ == "__main__":
    g = [[True, True, True, True, True, False],  # - - - - - X
         [False, False, False, False, True, False],  # X X X X - X
         [True, True, True, True, True, False],  # X X X X - X
         [True, False, False, False, True, False],  # X X X X - X
         [True, True, True, True, True, True]]  # X X X X - -
    print(robot_in_a_grid(g))
    print(robot_in_a_grid_optimized(g))
