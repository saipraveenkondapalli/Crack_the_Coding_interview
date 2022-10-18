"""
Sorted search : Given a sorted array like data structure with unknown length, find the index of a given element.
Assume that the array is sorted in increasing order.

"""

# Runtime Complexity: O(log n) because we are dividing the array in half each time
# Space Complexity: O(log n) because of the recursive calls otherwise O(1)


def search(arr, target):
    index = 1
    while arr[index] != -1 and arr[index] < target:
        index *= 2
    return binary_search(arr, target, index // 2, index)


def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target or arr[mid] == -1:
            right = mid - 1
        else:
            left = mid + 1
    return -1