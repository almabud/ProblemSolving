from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.dp_solution(nums, target)
    
    def dp_solution(self, nums: List[int], target: int, dp=[]) -> int:
        if not dp:
            dp = [-1] * 2000
        
        # Base case.
        if target == 0:
            return 1
        
        # If not meet the target.
        if target <= -1:
            return 0
        
        # Return from dp.
        if dp[target] != -1:
            return dp[target]
        
        ans = 0
        for num in nums:
            ans += self.dp_solution(nums, target-num, dp)
        
        dp[target] = ans

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum4([9], -1))
        