#O(N)
"""
s2 is rotation of s1
s1 = waterbottle
s2 = erbottlewat
s2 is roation of s1 so return true

"""
import unittest


def is_substring(s1,s2):
    return s1.find(s2) != -1


def isRotation(s1,s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1+s1,s2)


class Test(unittest.TestCase):
    dataT = [('waterbottle','erbottlewat'),('foo','ofo')] # True data which must return true
    dataF = [('waterbottle','erbottlewatt'),('foo','ofa')] # False data which must return false

    def test_isRotation(self):
        # true check
        for test_string, test_string2 in self.dataT:
            result = isRotation(test_string,test_string2)
            self.assertTrue(result)
        # false check
        for test_string, test_string2 in self.dataF:
            result = isRotation(test_string,test_string2)
            self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()


