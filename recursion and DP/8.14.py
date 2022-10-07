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
# Solution 1

def countEval(s, result):
    if len(s) == 0: return 0
    if len(s) == 1: return 1 if stringToBool(s) == result else 0
    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i+1:]
        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0
        if c == '^':
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
        subWays = totalTrue if result else total - totalTrue
        ways += subWays
    return ways

def stringToBool(s):
    return True if s == '1' else False

# Solution 2: Memoization
def countEval2(s, result, memo={}):
    if len(s) == 0: return 0
    if len(s) == 1: return 1 if stringToBool(s) == result else 0
    if (s, result) in memo: return memo[(s, result)]
    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i+1:]
        leftTrue = countEval2(left, True, memo)
        leftFalse = countEval2(left, False, memo)
        rightTrue = countEval2(right, True, memo)
        rightFalse = countEval2(right, False, memo)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0
        if c == '^':
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif c == '&':
            totalTrue = leftTrue * rightTrue
        elif c == '|':
            totalTrue = leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
        subWays = totalTrue if result else total - totalTrue
        ways += subWays
    memo[(s, result)] = ways
    return ways




if __name__ == "__main__":
    #print(countEval("1^0|0|1", False))
    print(countEval2("0&0&0&1^1|0^0", True))
    #print(countEval2("1^0|0|1", False))