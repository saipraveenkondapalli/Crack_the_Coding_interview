"""
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.
Anagram: A word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.
EXAMPLE
Input:  ['cinema', 'host', 'aba', 'train', 'doc', 'save', 'cafe', 'toes', 'set', 'dot', 'hamlet', 'act', 'tab', 'tac', 'listen', 'silent', 'part', 'hockey', 'leash', 'joke', 'boke', 'code']
Output: ['cinema', 'iceman', 'host', 'toes', 'save', 'doc', 'dot', 'act', 'tab', 'tac', 'train', 'part', 'cafe', 'leash', 'hamlet', 'hockey', 'listen', 'silent', 'joke', 'boke', 'code']
"""


def sort_chars(s):
    return ''.join(sorted(s))


def group_anagrams(arr):
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    d = {}
    for s in arr:
        key = sort_chars(s)
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]

    result = []
    for key in d:
        result.extend(d[key])
        # for s in d[key]:
        #     result.append(s)

    return result




if __name__ == "__main__":
    arr = ['cinema', 'host', 'iceman', 'osth', 'sai', 'praveen', 'kiran', 'iceman']
    ans = (group_anagrams(arr))
    print(ans)

