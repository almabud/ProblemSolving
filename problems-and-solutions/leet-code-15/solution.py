from typing import List


# Unsolved Can't remove the duplicates
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threesum_n_square(nums)

    def threesum_n_square(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = set()
        while i<len(nums):
            pointer1 = i+1
            pointer2 = len(nums) - 1
            while pointer1<pointer2:
                if nums[pointer1] + nums[pointer2] + nums[i] == 0:
                    res.add((nums[i], nums[pointer1], nums[pointer2]))
                    pointer1 += 1
                    pointer2 -= 1
                elif nums[pointer1] + nums[pointer2] + nums[i] > 0:
                    pointer2 -= 1
                else:
                    pointer1 += 1
            i += 1
        
        return res


    

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0,0,0,0]))
        
