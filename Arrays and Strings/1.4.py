"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.

Example:
Input: Tact Coa
Output: True (permutations: "taco cat", "atco cta", etc.)

"""
import unittest

# Book Solution 1

def isPalindromePermutation(string):
    # Run time O(n) Space O(1)
    # Assuming the string is ASCII

    string = string.lower()
    letters = [0] * 128

    # count the frequency of each character

    for char in string:
        if char != " ":
            letters[ord(char)] += 1
    odd = 0
    for i in letters:
        if i % 2 == 1:
            odd += 1
    return odd <= 1

# Book Solution 2

def isPalindromePermutation2(string):
    # Run time O(n) Space O(1)
    # Assuming the string is ASCII
    # instead running through the string twice, we can run through it once and keep track of the number of odd characters
    string = string.lower()
    letters = [0] * 128
    # count the frequency of each character
    odd = 0

    for char in string:
        if char != " ":
            letters[ord(char)] += 1
            if letters[ord(char)] % 2 == 1:
                odd += 1
            else:
                odd -= 1

    return odd <= 1





class Testcase(unittest.TestCase):
    # Test Cases
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]
    

    def test_isPalindromePermutation(self):
        for [test_string, expected] in self.data:
            actual = isPalindromePermutation(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
    print(isPalindromePermutation2("Tact Coa"))
