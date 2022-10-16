"""
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
Anagram: A word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
EXAMPLE
Input:  ['cinema', 'host', 'aba', 'train', 'doc', 'save', 'cafe', 'toes', 'set', 'dot', 'hamlet', 'act', 'tab', 'tac', 'listen', 'silent', 'part', 'hockey', 'leash', 'joke', 'boke', 'code']
Output: ['cinema', 'iceman', 'host', 'toes', 'save', 'doc', 'dot', 'act', 'tab', 'tac', 'train', 'part', 'cafe', 'leash', 'hamlet', 'hockey', 'listen', 'silent', 'joke', 'boke', 'code']
"""


def sortChars(s):
    return ''.join(sorted(s))


def groupAnagrams(arr):
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    d = {}
    for s in arr:
        key = sortChars(s)
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]

    result = []
    for key in d:
        for s in d[key]:
            result.append(s)

    return result




if __name__ == "__main__":
    arr = ['cinema', 'host', 'iceman', 'osth', 'sai', 'praveen', 'kiran', 'iceman']
    ans = (groupAnagrams(arr))
    print(ans)
    print(len(ans), len(arr))