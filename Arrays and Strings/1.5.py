"""Given two strings, write method to check if they are one edit awat from each other."""
import unittest


# book solution 1


def oneEditAway(s1,s2):
    # Run time O(n) Space O(1)
    # Assuming the string is ASCII
    if len(s1) == len(s2):
        return oneEditReplace(s1,s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1,s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s2,s1)
    return False

def oneEditReplace(s1,s2):
    diff = False
    for x in range(len(s1)):
        if s1[x] != s2[x]:
            if diff:
                return False
            diff = True
    return True

def oneEditInsert(s1,s2):
    index1 = 0 
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):

        if s1[index1] != s2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    

    return True



# Book solution 2

def oneEditAway2(s1,s2):
    # Runtime O(n) Space O(1)
    # Assuming the string is ASCII
    if abs(len(s1) - len(s2)) > 1:
        return False
    s1 = s1 if len(s1) < len(s2) else s2
    s2 = s2 if len(s1) < len(s2) else s1
    index1 = 0
    index2 = 0
    diff = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if diff:
                return False
            diff = True
            if len(s1) == len(s2):
                index1 += 1
        else:
            index1 += 1
        index2 += 1
    return True






class TestCases(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]   

    def test_oneEditAway(self):
        for [s1,s2,expected] in self.data:
            actual = oneEditAway(s1,s2)
            self.assertEqual(actual,expected)


if __name__ == "__main__":
    unittest.main()


