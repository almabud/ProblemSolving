# [Leet-code-377] Combination Sum IV

### Implementation:

```python
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
```

### Time complexity:

Time complexity is $O(target * nums)$
