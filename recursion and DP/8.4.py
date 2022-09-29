"""
Power set: Write a method to return all subsets of a set.
Example:
Input: {1, 2, 3}
Output: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}

"""


def power_set(set):
    if len(set) == 0:
        return [[]]
    else:
        subset = power_set(set[:-1])
        print(subset)
        return subset + [item + [set[-1]] for item in subset]  # add the last element to each subset


if __name__ == "__main__":
    print(power_set([1, 2, 3]))  # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
