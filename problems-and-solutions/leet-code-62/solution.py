class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.dp_unique_paths(m-1, n-1)

    def dp_unique_paths(self, m: int, n: int, dp=[]) -> int:
        # Initialize the dp.
        if not dp:
            dp = [[-1 for x in range(n+1)] for y in range(m+1)]
        # Base case.
        if m == 0 or n == 0:
            return 1
        # Return from the dp.
        if dp[m][n] != -1:
            return dp[m][n]

        ans = self.dp_unique_paths(m-1, n, dp) + self.dp_unique_paths(m, n-1, dp)
        # Store the ans in the dp.
        dp[m][n] =  ans

        return dp[m][n]



if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))