# move all negative number to end of the array

def move_neg(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1

    return arr


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    print(move_neg(arr))

