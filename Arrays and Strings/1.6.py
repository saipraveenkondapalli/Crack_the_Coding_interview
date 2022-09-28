"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

"""

# book solution 1

import unittest


def stringcompression(string):
    # run time O(p + k**2) where p is the size of the original string and k is the number of character sequences
    compressed = ''
    count = 0
    n = len(string)
    for x in range(n):
        count += 1
        if x+1 >= n or string[x] != string[x+1]:
            compressed += string[x] + str(count)
            count = 0
    return compressed if len(compressed) < n else string

# book solution 2
def stringcompression2(string):
    compressed = []
    count = 0
    n= len(string)
    for x in range(n):
        count += 1
        if x+1 >= n or string[x] != string[x+1]:
            compressed.append(string[x])
            compressed.append(str(count))
            count = 0
    compressed = ''.join(compressed)
    return compressed if len(compressed) < n else string


# book solution 3
def compressedString3(string):
    final_length = countCompression(string)
    if final_length >= len(string):
        return string
    compressed = []
    count = 0
    n = len(string)
    for x in range(n):
        count += 1
        if x+1 >= n or string[x] != string[x+1]:
            compressed.append(string[x])
            compressed.append(str(count))
            count = 0
    return ''.join(compressed)


# wrapper function for stringcompression3
def countCompression(string):
    compressed_length = 0
    count = 0
    n = len(string)
    for x in range(n):
        count += 1
        if x+1 >= n or string[x] != string[x+1]:
            # 1 for the character and 1 for the count of the character, alternatively you can use 
            #  "1 + len(str(count))""
            compressed_length += 2 
            count = 0
    return compressed_length


class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa','a2b1c5a3'),
        ('abcdef','abcdef'),
        ('aabbcc','aabbcc'),
        ('aaabbbccc','a3b3c3'),
        ('aaabbbcccddd','a3b3c3d3')]

    def test_stringcompression(self):
        for [string,expected] in self.data:
            actual = stringcompression2(string)
            self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()

