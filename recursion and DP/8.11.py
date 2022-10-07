"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent),
write code to calculate the number of ways of representing n cents.
"""



def makechange(n):
    denoms = [25,10,5,1]
    return change(n, denoms, 0)


def change(amount, denoms, index):
    if index >= len(denoms)-1: return 1
    ways = 0
    i = 0
    denoAmount = denoms[index]
    while i * denoAmount <= amount:
        remain = amount - i * denoAmount
        ways += change(remain, denoms, index+1)
        i += 1

    return ways


if __name__ == "__main__":
    print(makechange(10))
    print(N)
