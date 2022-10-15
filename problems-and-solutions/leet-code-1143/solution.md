# [Leet-code-1143] Longest Common Subsequence

### Discussion:

[LCS](../../Algorithms/dp/lcs/lcs.md)

### Implementation:

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, index_i=0, index_j=0, dp=[]) -> int:
        # dp initialization.
        if not dp:
            dp = [[-1 for x in range(len(text2))] for y in range(len(text1))]

        # Best case.
        if index_i >= len(text1) or index_j >= len(text2):
            return 0
        # Dp returning.
        if dp[index_i][index_j] != -1:
            return dp[index_i][index_j]
        
        # Declare the ans
        ans = 0
        # Check if the both index char is same.
        if text1[index_i] == text2[index_j]:
            ans = 1 + self.longestCommonSubsequence(text1, text2, index_i+1, index_j+1, dp)
        else:
            ans = max(
                self.longestCommonSubsequence(text1, text2, index_i, index_j+1, dp),
                self.longestCommonSubsequence(text1, text2, index_i+1, index_j, dp)
            )
        
        # Store the result into the dp.
        dp[index_i][index_j] = ans

        # Return the res.
        return ans
```

### Time complexity:

$O(N * M)$

> [Source code](solution.py)
