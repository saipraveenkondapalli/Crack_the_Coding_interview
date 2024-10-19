"""
Leetcode Unique Paths
"""


class Solution:
    def __init__(self):
        pass

    def UniquePaths(self, m, n):
        """
        :param m: int
        :param n: int
        :return: int
        """
        memo = [[-1] * n for _ in range(m)]

        for i in range(m):
            memo[i][0] = 1  # first column
        for j in range(n):
            memo[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]


# unique paths II
class Solution2:
    def uniquePathsWithObstacles(self, grid) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # first row
        for j in range(1, n):
            dp[0][j] = 1 if grid[0][j] == 0 and dp[0][j - 1] == 1 else 0

        # first column
        for i in range(1, m):
            dp[i][0] = 1 if grid[i][0] == 0 and dp[i - 1][0] == 1 else 0

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:  # obstacle
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.UniquePaths(3, 3))
    path = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s2 = Solution2()
    print(s2.uniquePathsWithObstacles(path))
