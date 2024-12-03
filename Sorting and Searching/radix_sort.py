"""
Radix Sort:
    - Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.
    - Time Complexity: O(nk) where n is the number of elements and k is the number of digits in the largest element.
    - Space Complexity: O(n+k) where n is the number of elements and k is the number of digits in the largest element.
    - Stable: Yes
    - In-Place: Yes
"""
# Algorithm explanation: https://www.youtube.com/watch?v=XiuSW_mEn7g
# Demo of radix sort: https://www.youtube.com/watch?v=nu4gDuFabIM
def _counting_sort(arr: list, exp: int):
    output = [0] * len(arr)
    count = [0] * 10

    # Count occurrences of each digit
    for i in range(len(arr)):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]


def _radix_sort(arr: list):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        _counting_sort(arr, exp)
        exp *= 10


def radix_sort(arr: list):
    # Separate positive and negative numbers
    pos = [x for x in arr if x >= 0]
    neg = [abs(x) for x in arr if x < 0]

    # Sort positive numbers
    _radix_sort(pos)

    # Sort negative numbers (in reverse order)
    if neg:
        _radix_sort(neg)
        neg.reverse()  # Reverse to get the correct order

    # Combine negative and positive numbers
    return [-x for x in neg] + pos


if __name__ == "__main__":
    arr = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, -9]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)
