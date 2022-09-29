
def multiply(m,n):
    n = max(m,n)
    m = min(m,n)
    return multiply_helper(n,m)


def multiply_helper(n,m):
    if m == 0:return 0
    return n+multiply_helper(n,m-1)


if __name__ == "__main__":

    print(multiply(6,500))

