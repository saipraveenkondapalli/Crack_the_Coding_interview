"""
Magic Index: A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
"""


# Solution 1, Assuming the array is sorted and distinct
def magic_index(array):
    left = 0
    right = len(array) - 1
    return magic_index_helper(array, left, right)


def magic_index_helper(array, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return magic_index_helper(array, mid + 1, right)
    else:
        return magic_index_helper(array, left, mid - 1)


# Solution 2, Assuming the array is sorted and not distinct
def magic_index_not_distinct(array):
    left = 0
    right = len(array) - 1
    return magic_index_helper_not_distinct(array, left, right)


def magic_index_helper_not_distinct(array, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    if array[mid] == mid:
        return mid
    left_index = min(mid - 1, array[mid])
    left = magic_index_helper_not_distinct(array, left, left_index)
    if left:
        return left
    right_index = max(mid + 1, array[mid])
    right = magic_index_helper_not_distinct(array, right_index, right)
    return right


if __name__ == "__main__":
    array = [-1, -2, 0, 3, 7, 8, 10, 11, 15]
    print(magic_index(array))  # 3
    array = [-1, -2, 0, 3, 3, 3, 3, 3, 3]
    print(magic_index_not_distinct(array))  # 3
