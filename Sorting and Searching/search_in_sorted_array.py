"""
Search in rotated array: Given a sorted array of n integers that has been rotated
an unknown number of times, write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
EXAMPLE
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
"""


# Runtime Complexity: O(log n) because we are dividing the array in half each time
# Space Complexity: O(log n) because of the recursive calls otherwise O(1)
def search(arr, target, left, right):
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if left > right:
        return -1

    if arr[mid] > arr[left]: # left side is sorted
        if arr[left] <= target < arr[right]:
            return search(arr, target, left, mid - 1)  # Search left
        else:
            return search(arr, target, mid + 1, right)  # Search right
    elif arr[mid] < arr[left]: # Right is sorted
        if arr[mid] < target <= arr[right]: # Search right
            return search(arr, target, mid + 1, right)
        else:
            return search(arr, target, left, mid - 1) # Search left
    elif arr[mid] == arr[left]: # Left side is all repeats
        if arr[mid] != arr[right]: # If right is different, search it
            return search(arr, target, mid + 1, right) # Search right
        else:
            result = search(arr, target, left, mid - 1) # Search left
            if result == -1: # If not found, search right
                return search(arr, target, mid + 1, right) # Search right
            else:
                return result # Found in left side
    return -1 # Not found


if __name__ == "__main__":
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(search(arr, 54, 0, len(arr) - 1))