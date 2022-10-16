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


def radix_sort(arr: list):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr: list, exp: int):
    output = [0] * len(arr)
    count = [0] * 10

    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


if __name__ == "__main__":
    arr = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, 9]
    radix_sort(arr)
    print(arr)
