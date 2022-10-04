"""
Tower of Hanoi: In the classic problem of the Tower of Hanoi, you have 3 towers
and N disks of different sizes which can slide onto any tower. The puzzle starts
with disks sorted in ascending order of size from top to bottom (i.e., each disk
sit on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.
"""


def tower_of_hanoi(n, source, dest, buffer):
    if n == 1:
        dest.append(source.pop())
        return
    tower_of_hanoi(n - 1, source, buffer, dest)
    dest.append(source.pop())
    tower_of_hanoi(n - 1, buffer, dest, source)
    return dest


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    B = []
    C = []
    print(tower_of_hanoi(len(A), A,B,C))
