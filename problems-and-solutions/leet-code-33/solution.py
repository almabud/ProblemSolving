from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.solution_in_log_n_binary_search_way(nums, target)

    def solution_in_n(self, nums: List[int], target: int) -> int:
        for key, val in enumerate(nums):
            if val == target:
                return key

    def solution_in_log_n_merge_sort_way(self, nums: List[int], target: int, left=None, right=None) -> int:
        left = 0 if left is None else left
        right = len(nums) - 1 if right is None else right
        if left >= right:
            return left if (nums[left] == target) or (nums[right] == target) else -1
        
        # Calculate the mid
        mid = int(left + (right - left)/2)
        # Call the merge portion
        left = self.solution_in_log_n_merge_sort_way(nums, target, left, mid)
        right = self.solution_in_log_n_merge_sort_way(nums, target, mid+1, right)

        if nums[left] == target and left > -1:
            return left
        elif nums[right] == target and right > -1:
            return right
        else:
            return -1
    
    def solution_in_log_n_binary_search_way(self, nums: List[int], target: int, left=None, right=None) -> int:
        left = 0 if left is None else left
        right = len(nums) - 1 if right is None else right

        if left >= right:
            return left if (nums[left] == target) or (nums[right] == target) else -1

        mid = int(left + (right - left)/2)
        if nums[left] <= nums[mid] and nums[left] <= target <= nums[mid]:
            # Left part is sorted and target is in left part
            return self.solution_in_log_n_binary_search_way(nums, target, left, mid)

        elif nums[mid+1] <= nums[right] and nums[mid+1] <= target <= nums[right]:
            # Right part is sorted and target is in right part.
            return self.solution_in_log_n_binary_search_way(nums, target, mid+1, right)
        else:
            if nums[left] < nums[mid]:
                # Solution is right unsorted part
                return self.solution_in_log_n_binary_search_way(nums, target, mid+1, right)
            # Solution is in left unsorted part
            return self.solution_in_log_n_binary_search_way(nums, target, left, mid)


if __name__ == "__main__":
    s = Solution()
    print(s.search([1,3], 3))