from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.house_rob_dp(nums)
    
    def house_rob_dp(self, nums: List[int], index=0, dp=[]) -> int:
        # Initialize the dp.
        if not dp:
            dp = [-1] * 500
        
        if index >= len(nums):
            return 0
        if dp[index] != -1:
            return dp[index]

        ans1 = 0
        ans2 = 0
        ans1 += nums[index] + self.house_rob_dp(nums, index+2, dp)
        ans2 += self.house_rob_dp(nums, index+1, dp)
        # Store in dp.
        dp[index] = max(ans1, ans2)
        
        return dp[index]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1,2,3,1]))
        

        