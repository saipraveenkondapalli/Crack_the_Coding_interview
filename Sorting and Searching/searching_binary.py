"""
Binary search is a search algorithm that finds the position of a target value
within a sorted array. Binary search compares the target value to the middle
element of the array. If they are not equal, the half in which the target cannot
lie is eliminated and the search continues on the remaining half, again taking
the middle element to compare to the target value, and repeating this until the
target value is found. If the search ends with the remaining half being empty,
the target is not in the array.
"""
# Algorithm explanation: https://www.youtube.com/watch?v=P3YID7liBug


def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2  # // is integer division (rounds down)
        if arr[mid] == target:  # Found the target
            return mid
        elif arr[mid] < target:  # Target is in the right half
            low = mid+1
        else:
            high = mid-1  # Target is in the left half

    return -1  # Target not found


# Recursive implementation
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found
    mid = (low+high)//2 # // is integer division (rounds down)
    if arr[mid] == target:
        return mid
    elif arr[mid] < target: # Target is in the right half
        return binary_search_recursive(arr, target, mid+1, high)
    else:
        return binary_search_recursive(arr, target, low, mid-1) # Target is in the left half



