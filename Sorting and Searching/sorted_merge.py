"""
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B
Write a method to merge B into A in sorted order.
EXAMPLE
Input:
A = [1, 3, 5, 7, 9, 0, 0, 0, 0, 0]
B = [2, 4, 6, 8, 10]
Output: A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
#  Time Complexity: O(n)
#  Space Complexity: O(1)


def merge(A,B):
    i = len(A) - 1
    j = len(B) - 1
    k = len(A) + len(B) - 1
    A = A + [0] * len(B)  # Add extra space to A to hold B as python lists dynamically resize
    while j >=0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    return A


if __name__ == "__main__":
    A = [1, 3, 5, 7, 9]
    B = [2, 4, 6, 8, 10]
    print(merge(A, B))