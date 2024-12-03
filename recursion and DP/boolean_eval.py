"""
Boolean evaluation: Given a boolean expression consisting of the symbols 0 (false),
1 (true), & (AND), | (OR), and ^ (XOR), and a desired boolean result value result,
implement a function to count the number of ways of parenthesizing the expression
such that it evaluates to result. The expression should be fully parenthesized (e.g., (0)^(1))
but not extraneously (e.g., (((0))^(1))).
EXAMPLE
countEval("1^0|0|1", false) -> 2
countEval("0&0&0&1^1|0", true) -> 10
"""


def _calc_total_true(left_true, left_false, right_true, right_false, c):
    if c == '^':
        return left_true * right_false + left_false * right_true
    elif c == '&':
        return left_true * right_true
    elif c == '|':
        return left_true * right_true + left_true * right_false + left_false * right_true


# Solution 1
def count_eval(s, result):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if string_to_bool(s) == result else 0

    ways = 0

    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]

        left_true = count_eval(left, True)
        left_false = count_eval(left, False)
        right_true = count_eval(right, True)
        right_false = count_eval(right, False)

        total = (left_true + left_false) * (right_true + right_false)
        total_true = _calc_total_true(left_true, left_false, right_true, right_false, c)

        sub_ways = total_true if result else total - total_true
        ways += sub_ways

    return ways


def string_to_bool(s):
    return s == '1'


def count_eval2(s, result, memo=None):
    if memo is None:
        memo = {}

    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if string_to_bool(s) == result else 0

    if (s, result) in memo:
        return memo[(s, result)]

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]

        left_true = count_eval2(left, True, memo)
        left_false = count_eval2(left, False, memo)
        right_true = count_eval2(right, True, memo)
        right_false = count_eval2(right, False, memo)

        total = (left_true + left_false) * (right_true + right_false)
        total_true = _calc_total_true(left_true, left_false, right_true, right_false, c)

        sub_ways = total_true if result else total - total_true

        ways += sub_ways

    memo[(s, result)] = ways
    return ways


if __name__ == "__main__":
    # print(countEval("1^0|0|1", False))
    print(count_eval2("0&0&0&1^1|0^0", True))
    # print(countEval2("1^0|0|1", False))
