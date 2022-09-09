''' Given Two Strings, write a method to decide if one is a permutation of the other. '''

# my Sloution 1, book solution 1

def isPermutation1(s1, s2):
    # sort the strings and compare them
    # Run time O(nlogn) Space O(1)

    return False if len(s1) != len(s2) else sorted(s1) == sorted(s2)


# Book Solution 2

def isPermutation(s,t):
    # Run time O(s+t), Run time might be wrong check later Space O(1)
    if len(s) != len(t):
        return False
    
    letters = [0] * 128
    for char in s:
        letters[ord(char)] += 1
    
    for c in t:
        c = ord(c)
        letters[c] -= 1
        if letters[c] < 0:
            return False
    return True

print(isPermutation("abc", "cba"))




