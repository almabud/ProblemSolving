from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.LIS_n_log_n(nums)
    
    def find_LIS(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        ans = 0
        # Find the LIS for every position.
        for i, val in enumerate(nums):
            ans = max(ans, self.calculate_LIS(nums, i, dp))
        
        return ans

    def calculate_LIS(self, nums: List[int], index = 0, dp = []) -> int:
        # Return from dp
        if dp[index] != -1:
            return dp[index]
    
        # Declare res.
        ans = 0
        for i in range(index+1, len(nums)):
            if nums[i] > nums[index]:
                ans = max(ans, self.calculate_LIS(nums, i, dp))

        dp[index] = ans+1

        return dp[index]
    
    def LIS_n_log_n(self, nums: List[int]) -> int:
        # Define the max and min.
        max_int = 999999
        min_int = -999999

        # Initialize the LIS list
        lis = [max_int] * (len(nums) + 1)
        lis[0] = min_int

        def find_suitable_position(key):
            left = 0
            right = len(lis) - 1

            while right - left > 1:
                mid = left + (right - left) // 2

                if key <= lis[mid] <= max_int:
                    right = mid
                else:
                    left = mid
            
            return right
        
        # Find the LIS sequence
        for val in nums:
            lis[find_suitable_position(val)] = val
            print(lis)
        
        lis_length = 0
        for i, val in enumerate(lis):
            if val < max_int:
                lis_length = i
        
        return lis_length


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([4,10,15,3,5]))
