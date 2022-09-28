# Normal Recursion

def fib1(n):
    if n == 0 or n ==1 : return n
    else: return fib1(n-1) + fib1(n-2)


# Memoization
def fib2(n):
    memo = [-1] * (n+1)
    return fib2_helper(n, memo)


def fib2_helper(n, memo):
    if n == 0 or n == 1: return n
    if memo[n] != -1: return memo[n]
    memo[n] = fib2_helper(n-1, memo) + fib2_helper(n-2, memo)
    return memo[n]


# Bottom up Approach
def fib3(n):
    if n == 0 or n == 1: return n
    bottom_up = [0] * (n+1)
    bottom_up[1] = 1
    for i in range(2, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


#  Bottom up Approach with O(1) space
def fib4(n):
    if n == 0 or n == 1: return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b


if __name__ == "__main__":
    print(fib1(5))
    print(fib2(5))
    print(fib3(5))
    print(fib4(5))
