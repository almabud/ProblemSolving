from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        zero_indx = None
        prod = 1
        for key,val in enumerate(nums):
            if zero_count > 1:
                break
            if val == 0:
                zero_count += 1
                zero_index = key
                continue
            prod *= val
        
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = prod
            return res
        if zero_count > 1:
            return [0]*len(nums)
        
        return [int(prod/x) for x in nums]


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([-1,1,0,0,3]))
            