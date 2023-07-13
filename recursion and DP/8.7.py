"""
Permutations without dups - Write a method to compute all permutations of a string of unique characters.
Run time complexity: O(n!), where n is the length of the string
"""


def permutations(s):
    if len(s) == 1:
        return [s]  # base case, last character
    perms = permutations(s[1:])
    first_char = s[0]
    result = []
    for perm in perms: # for each permutation
        for i in range(len(perm)+1): # for each position in the permutation, add the first character
            result.append(perm[:i] + first_char + perm[i:])
    return result


if __name__ == "__main__":
    print(permutations("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

