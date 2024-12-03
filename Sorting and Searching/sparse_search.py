"""
Sparse Search: Given a sorted array of strings that is interspersed with empty strings,
               write a method to find the location of a given string.
EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4
"""


def sparse_search(arr: list, target: str) -> int:
    if not arr or not target:
        return -1

    return binary_search_mod(arr, target, 0, len(arr) - 1)


def binary_search_mod(arr: list, target: str, first: int, last: int) -> int:
    if first > last:
        return -1

    mid = (first + last) // 2

    if arr[mid] == "":
        left = mid - 1
        right = mid + 1

        while True:
            if left < first and right > last:
                return -1
            elif left >= first and arr[left] != "":
                mid = left
                break
            elif right <= last and arr[right] != "":
                mid = right
                break

            left -= 1
            right += 1

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search_mod(arr, target, mid + 1, last)
    else:
        return binary_search_mod(arr, target, first, mid - 1)


if __name__ == "__main__":
    arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(sparse_search(arr, "ball"))  # 4
