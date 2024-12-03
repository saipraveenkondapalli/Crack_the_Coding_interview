"""
Quick Sort
    - Divide and Conquer algorithm.
    - Pick an element, called a pivot, from the array.
    - Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position.
    - Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
    - Time Complexity: O(nlogn)
    - Space Complexity: O(logn)
    - Stable: No
    - In-Place: Yes
"""
# Algorithm explanation: https://www.youtube.com/watch?v=SLauY6PpjW4


def quick_sort(arr: list):
    _helper(arr, 0, len(arr)-1)


def _helper(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        _helper(arr, low, pivot-1)
        _helper(arr, pivot+1, high)


def partition(arr, low, high):
    pivot = arr[high] # pivot element
    i = low-1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap the elements
    arr[i+1], arr[high] = arr[high], arr[i+1] # place the pivot element in its correct position
    return i+1

def quick_sort2(arr: list):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] # Pick a pivot element midway through the list
    left = [x for x in arr if x < pivot] # All elements less than the pivot
    middle = [x for x in arr if x == pivot] # All elements equal to the pivot
    right = [x for x in arr if x > pivot] # All elements greater than the pivot

    return quick_sort2(left) + middle + quick_sort2(right)


if __name__ == "__main__":
    sample = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, 9]
    sample2 = sample.copy()
    print(quick_sort2(sample))

    quick_sort(sample2)
    print(sample2)
