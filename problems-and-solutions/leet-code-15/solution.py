from typing import List


# Unsolved Can't remove the duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threesum_in_n_square(nums)

    def threesum_in_n_square(self, nums: List[int]) -> List[List[int]]:
        mark_arr = {}
        for item in nums:
            if mark_arr.get(item):
                mark_arr[item] += 1
                continue
            mark_arr[item] = 1
        res = []
        # Find the 3 sum array
        for i in range(len(nums)):
            mark_arr[nums[i]] -= 1
            target_sum = -1 * nums[i]
            for k in range(i+1, len(nums)):
                search_val = target_sum - nums[k]
                if mark_arr.get(search_val) is None:
                    continue
                mark_arr[nums[k]] -= 1
                if mark_arr[search_val] > 0:
                    res.append([nums[i], nums[k], search_val])
                    mark_arr[search_val] -= 1
                if mark_arr[nums[k]] >= 1 and mark_arr[search_val] >= 1:
                    mark_arr[nums[k]] = 0
        return res
    

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0,0,0,0]))
        
