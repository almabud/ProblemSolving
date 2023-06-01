from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twosum_twopointer(nums,target)

    def twosum_hasmap(self, num: List[int], target: int) -> List[int]:
        dict_store = {value:key for key, value in enumerate(nums)}
        for key, val in enumerate(nums):
            search_val = target - val
            if dict_store.get(search_val) and key != dict_store.get(search_val):
                res = (key, dict_store.get(search_val))
                break
        
        return res
    
    def twosum_twopointer(self, nums: List[int], target: int) -> List[int]:
        # Sort the nums.
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        pointer1 = 0
        pointer2 = len(nums) - 1

        while pointer1 < pointer2:
            if nums[pointer1][1] + nums[pointer2][1] == target:
                return (nums[pointer1][0], nums[pointer2][0])
            if nums[pointer2][1]+nums[pointer1][1] > target:
                pointer2 -= 1
            else:
                pointer1 += 1
