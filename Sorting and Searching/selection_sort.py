"""
Selection sort
    - Find the minimum element in unsorted array
    - Swap the found minimum element with the first element
    - Repeat for the remaining elements
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    - Stable: No
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]



if __name__ == "__main__":
    arr = [456, 123, 789, 0, 1, 2, 3, 3, -5, 3, 7, 8, 9]
    selection_sort(arr)
    print(arr)
