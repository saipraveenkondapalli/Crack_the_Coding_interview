"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
"""


def make_change(n):
    denoms = [25, 10, 5, 1]
    ways, amounts = change(n, denoms, 0)
    return ways, amounts


def change(amount, denoms, index):
    if index >= len(denoms) - 1:
        return 1, [[1] * amount]
    ways = 0
    all_amounts = []
    i = 0
    deno_amount = denoms[index]
    while i * deno_amount <= amount:
        remain = amount - i * deno_amount
        sub_ways, sub_amounts = change(remain, denoms, index + 1)
        ways += sub_ways
        for sub_amount in sub_amounts:
            all_amounts.append([deno_amount] * i + sub_amount)
        i += 1
    return ways, all_amounts


if __name__ == "__main__":
    w, a = make_change(50)
    print(f"Number of ways: {w}")
    print(*a, sep="\n")
