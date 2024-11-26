"""
Power set: Write a method to return all subsets of a set.
Example:
Input: {1, 2, 3}
Output: {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}

Time Complexity: O(n*2^n)

"""


def power_set(set):
    if len(set) == 0:
        return [[]]
    else:
        subset = power_set(set[:-1])
        last_set = set[-1:]
        new_set = [x + last_set for x in subset]
        return subset + new_set


def power_set_recursion(data):
    res = []

    def backtrack(start, path):
        res.append(path)

        for i in range(start, len(data)):
            backtrack(i + 1, path + [data[i]])

    backtrack(0, [])
    return res


if __name__ == "__main__":
    print(power_set([1, 2, 3]))  # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    print(power_set_recursion([1, 2, 3]))  # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
