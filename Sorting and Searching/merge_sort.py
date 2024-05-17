"""
Merge Sort:
    - Divide and Conquer algorithm.
    - Divide the unsorted list into n sub lists, each containing 1 element (a list of 1 element is considered sorted).
    - Repeatedly merge sub lists to produce new sorted sub lists until there is only 1 sublist remaining. This will be the sorted list.
    - Time Complexity: O( nlogn )
    - Space Complexity: O(n)
    - Stable: Yes
    - In-Place: No (requires extra space)
"""


# Algorithm explanation: https://www.youtube.com/watch?v=MZaf_9IZCrc


def merge_sort(arr: list):
    help = []
    _helper(arr, help, 0, len(arr) - 1)


def _helper(arr, help, low, high):
    if low < high:
        mid = (low + high) // 2
        _helper(arr, help, low, mid)
        _helper(arr, help, mid + 1, high)
        merge(arr, help, low, mid, high)


def merge(arr, help, low, mid, high):
    # Copy both parts into the help array
    for i in range(low, high + 1):
        help.append(arr[i])
    helper_left = low
    helper_right = mid + 1
    current = low
    # Iterate through the help array. Compare the left and right half, copying back the smaller element from the two
    # halves into the original array.
    while helper_left <= mid and helper_right <= high:
        if help[helper_left] <= help[helper_right]:
            arr[current] = help[helper_left]
            helper_left += 1
        else:
            arr[current] = help[helper_right]
            helper_right += 1
        current += 1
    # Copy the rest of the left side of the array into the target array
    remaining = mid - helper_left
    for i in range(remaining + 1):
        arr[current + i] = help[helper_left + i]


if __name__ == "__main__":
    sample_arr = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, 9]
    merge_sort(sample_arr)
    print(sample_arr)
