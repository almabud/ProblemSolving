# Solution with O(n)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0

        for val in nums:
            sum += val
            max_sum = max(sum, max_sum)
            if sum < 0:
                sum = 0
        return max_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([1, -1]))