"""
Missing Int: Given an input file with four billion non-negative integers,
            provide an algorithm to generate an integer that is not contained in the file.
            Assume you have 1 GB of memory available for this task.

FOLLOW UP
            What if you have only 10 MB of memory?
            Assume that all the values are distinct, and
            we now have no more than one billion non-negative integers.
"""

"""
Approach:
    - Since we have 1 GB of memory available, we can use a bit vector to represent the integers.
    - 1 GB = 8 billion bits // 
    - We can represent 4 billion integers using 4 billion bits.
    - We can use a bit vector to represent the integers.
    - All bits are initialized to 0.
    - For each integer, we set the corresponding bit to 1.
    - Finally, we scan the bit vector to find the first bit that is 0.
    - The index of this bit is the missing integer.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

def find_missing_int(file_path):
    INT_SIZE = 8
    arr = [0] * (2 ** 31 // INT_SIZE)
    with open(file_path, 'r') as file:
        for line in file:
            num = int(line)
            arr[num // INT_SIZE] |= 1 << (num % INT_SIZE)
    for i in range(len(arr)):
        for j in range(INT_SIZE):
            if arr[i] & 1 << j == 0:
                return i * INT_SIZE + j
    return -1




if __name__ == "__main__":
    file_path = "missing_int.txt"
    print(find_missing_int(file_path))
    # Output: 2147483648
    # The missing integer is 2^31 = 2147483648

