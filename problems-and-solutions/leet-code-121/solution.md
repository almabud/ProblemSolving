```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = 1000000
        for val in prices:
            profit = val - min_price
            max_profit = profit if profit>max_profit else max_profit
            min_price = val if min_price > val else min_price
        return max_profit
```
