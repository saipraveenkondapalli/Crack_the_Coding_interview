"""
8.10:Paint Fill
Run time: O(n)
Space complexity: O(n)
"""


def PaintFill(screen, r, c, new_color):  # r,c are the row and column of the pixel clicked by the user
    # ncolor is the new color to be filled
    if screen[r][c] == new_color:
        return False
    visited = [[False for _ in range(len(screen[0]))] for _ in range(len(screen))]
    return fillColor(screen, r, c, screen[r][c], new_color,  visited)


def fillColor(screen, r, c, original_color, new_color, visited):
    if r < 0 or c < 0 or r > len(screen) - 1 or c > len(screen[0]) - 1:  # handling border conditions
        return False

    if visited[r][c]:
        return
    visited[r][c] = True

    if screen[r][c] == original_color:
        screen[r][c] = new_color
        fillColor(screen, r - 1, c, original_color, new_color, visited)  # top
        fillColor(screen, r + 1, c, original_color, new_color, visited)  # down
        fillColor(screen, r, c + 1, original_color, new_color, visited)  # right
        fillColor(screen, r, c - 1, original_color, new_color, visited)  # left

    return screen


if __name__ == "__main__":
    demo = [
        ["blue", "blue", "blue"],
        ["green", "blue", "blue"],
        ["blue", "red", "blue"],
    ]
    # Original Screen
    for i in demo:
        print(i)
    print()
    # New Screen
    for i in PaintFill(demo, 1, 1, "yellow"):
        print(i)
    print()
