from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            self.circular_robing(nums, len(nums) - 1, 0),
            self.circular_robing(nums, len(nums), 1)
        )
    
    def circular_robing(self, nums: List[int], length: int, index: int, dp=[]) -> int:
        if not dp:
            dp = [-1] * len(nums)
        # Base case for lenght 1.
        if len(nums) == 1:
            return nums[0]
        # Basecase.
        if index >= length:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        ans = nums[index] + self.circular_robing(nums, length, index+2, dp)
        ans1 = self.circular_robing(nums, length, index+1, dp)

        dp[index] = max(ans, ans1)
        
        return dp[index]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([2]))
        