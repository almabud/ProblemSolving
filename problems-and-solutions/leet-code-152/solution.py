from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
            max(reverse_prod, forward_prod)
        """

        max_prod1 = max_prod2 = -999999
        prod1 = prod2 = 1
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            prod1 *= nums[i]
            prod2 *= nums[j]
            max_prod1 = max(prod1, max_prod1)
            max_prod2 = max(prod2, max_prod2)

            prod1 = 1 if prod1 == 0 else prod1
            prod2 = 1 if prod2 == 0 else prod2

            i += 1
            j -= 1
        
        return max(max_prod1, max_prod2)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([-3,0,1,-2]))