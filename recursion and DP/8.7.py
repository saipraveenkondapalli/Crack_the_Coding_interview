"""
Permutations without dups - Write a method to compute all permutations of a string of unique characters.

"""


def permutations(s):
    if len(s) == 1: return [s]
    perms = permutations(s[1:])
    char = s[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result


if __name__ == "__main__":
    print(permutations("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

