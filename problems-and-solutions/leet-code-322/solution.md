```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * 100000
        res = self.coin_change_with_dp(coins, amount, dp)
        return res if res < 9999999 else -1

    def coin_change_with_dp(self, coins: List[int], amount:int, dp: List[int]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return 9999999
        if dp[amount] != -1:
            return dp[amount]
        
        ans = 9999999
        for i in coins:
            ans = min(ans, 1 + self.coin_change_with_dp(coins, amount-i, dp))
        
        dp[amount] = ans
        
        return ans
```
