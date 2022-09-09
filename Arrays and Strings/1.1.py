# is Unique, check whether a string has all unique characters

# my solution 1, the below solution is wrong, fix it later
"""
def isUnique1(s):
    # Run time O(n^2) Space O(1)
    n = len(s)
    for x in range(n):
        for y in range(x, n):
            if s[x] == s[y]:
                return False
    
    return True

"""

# my solution 2
def isUnique2(s):
    # sort the string and check if the next character is the same as the current character
    # Run time O(nlogn) Space O(1)
    s = sorted(s)
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            return False
    return True


# book solution 1

def isUnique3(s):
    # consider Ascii values, 256 characters
    # Run time O(n) Space O(1)
    if len(s) > 256:
        return False # if string is longer than 256 characters, it must have repeated characters
    char_set = [False] * 256 # create a list of 256 False values
    for char in s:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True


# book solution 2

def isUnique4(s):
    # use bit vector method 
    # Run time O(n) Space O(1)
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True





if __name__ == "__main__":
    s = "abcdefg"
   # print(isUnique1(s))
    print(isUnique2(s))
    print(isUnique3(s))
    print(isUnique4(s))
