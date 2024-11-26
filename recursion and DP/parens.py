"""
Parens : Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""


def parens(n):
    """
    Solution Optimized
    Runtime: O(2^n) because we are doing 2 recursive calls each time until we reach the base case ,but avoid duplicates
    so it is slightly  less than 2^n
    """
    result = []
    parens_helper(n, n, "", result)
    return result


def parens_helper(left, right, s, result):
    if left == 0 and right == 0:
        result.append(s)
        return
    if left > 0:
        parens_helper(left - 1, right, s + "(", result)
    if right > left:
        parens_helper(left, right - 1, s + ")", result)


# Solution 2

def solution2(remaining):
    result = set()
    if remaining == 0:
        result.add("")
    else:
        partials = solution2(remaining - 1)
        for s in partials:
            for i in range(len(s)):
                if s[i] == "(":
                    s2 = insert_inside(s, i)
                    result.add(s2)
            result.add(s + "()")
    return result


def insert_inside(s, left_index):
    left = s[:left_index + 1]
    right = s[left_index + 1:]
    return left + "()" + right


if __name__ == "__main__":
    print(parens(3))  # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(solution2(3))
