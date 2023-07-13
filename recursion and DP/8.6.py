"""
Tower of Hanoi: In the classic problem of the Tower of Hanoi, you have 3 towers
and N disks of different sizes which can slide onto any tower. The puzzle starts
with disks sorted in ascending order of size from top to bottom (i.e., each disk
sit on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.

Runtime: O(2^n) because we are doing 2 recursive calls each time until we reach the base case.
"""


def tower_of_hanoi(n, source, dest, buffer):
    if n <= 0: return
    tower_of_hanoi(n-1, source, buffer, dest)
    dest.append(source.pop())
    tower_of_hanoi(n-1, buffer, dest, source)
    return dest


if __name__ == "__main__":
    n = 5
    source = [i for i in range(n, 0, -1)] # [5, 4, 3, 2, 1]
    dest = []
    buffer = []
    print(source, dest, buffer)
    print(tower_of_hanoi(n, source, dest, buffer))
