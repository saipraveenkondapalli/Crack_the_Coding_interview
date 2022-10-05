"""
8.10:Paint Fill
"""

def PaintFill(screen, r,c, ncolor):
    # ncolor is the new color to be filled
    if screen[r][c] == ncolor: return False
    return fillColor(screen, r,c, screen[r][c], ncolor)

def fillColor(screen, r,c, cColor, ncolor):
    # cColor is Current Color, ncolor is the new color to be filled

    if (r <0 or c<0 or r> len(screen)-1 or c > len(screen[0])-1): # hanlding border conditions
        return False
    print(r,c)
    if screen[r][c] == cColor:
        screen[r][c] = ncolor
        fillColor(screen, r - 1, c, cColor, ncolor) # top
        fillColor(screen, r+1, c-1, cColor, ncolor) # down
        fillColor(screen, r, c+1, cColor, ncolor) # right
        fillColor(screen, r, c-1, cColor, ncolor) # left

    return screen


if __name__ == "__main__":
    screen = [
        ["blue","blue","blue"],
        ["green","blue","blue"],
        ["red", "red", "blue"],
    ]



