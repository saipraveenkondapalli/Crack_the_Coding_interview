"""
Triple Steps: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""


def triple_steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return triple_steps(n - 1) + triple_steps(n - 2) + triple_steps(n - 3)


# Memoization
def triple_step_optimized(n):
    memo = [-1] * (n + 1)
    return triple_steps_optimized_helper(n, memo)


def triple_steps_optimized_helper(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = (triple_steps_optimized_helper(n - 1, memo) +
                   triple_steps_optimized_helper(n - 2, memo) +
                   triple_steps_optimized_helper(n - 3, memo))
        return memo[n]


if __name__ == "__main__":
    print(triple_steps(3))  # 4
    print(triple_step_optimized(3))  # 4
