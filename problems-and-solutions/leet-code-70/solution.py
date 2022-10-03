from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        return self.count_distinct_way(n, dp)

    def count_distinct_way(self, n: int, dp: List[int]) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        if dp[n]:
            return dp[n]
        
        cal1 = self.count_distinct_way(n - 1, dp)
        cal2 = self.count_distinct_way(n - 2, dp)
        # Store the dp
        if n-1 >= 0:
            dp[n-1] = cal1
        if n-2 >= 0:
            dp[n-2] = cal2
       
        return cal1 + cal2


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(0))