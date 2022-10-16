"""
Bubble Sort:
    - Repeatedly swap the adjacent elements if they are in wrong order.
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    - Stable: Yes
    - In-Place: Yes
"""
# Demo of bubble sort: https://www.youtube.com/watch?v=yIQuKSwPlro/


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    arr = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, 9]
    bubble_sort(arr)
    print(arr)
