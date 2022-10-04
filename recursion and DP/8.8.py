"""
permutation with dups: Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

"""
# Ineffienct but works, use a set to remove duplicates
def permutations(s):
    if len(s) == 1: return [s]
    perms = permutations(s[1:])
    char = s[0]
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return list(set(result))




if __name__ == "__main__":
    print(permutations("aab")) # ['aab', 'aba', 'baa', 'aaa', 'baa', 'aba'], duplicates are removed by set() # ['aab', 'aba', 'baa', 'aaa']
    print(permutations("aabbbbc"))