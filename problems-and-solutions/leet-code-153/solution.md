```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.find_min_bi_search_way_in_log_n(nums)

    def find_min_in_n(self, nums: List[int]) -> int:
        min_element = 999999999
        for val in nums:
            min_element = min(min_element, val)
        
        return min_element
    
    def find_min_in_log_n(self, nums: List[int], left=None, right=None) -> int:
        """
        This is the merge sort way. We will devide the array until there is only one element.
        Then we return the minmum from left part and right part. We are deviding the array
        and comparing the array so time complexity
        T = 2*T(n/2) + 1 = O(logn)
        """

        left = 0 if left is None else left
        right = len(nums)-1 if right is None else right
        
        # Calculate the mid
        mid = left + int((right - left)/2)

        # Base case
        if left == right:
            return nums[left]

        left_part_min = self.find_min_in_log_n(nums, left, mid)
        right_part_min = self.find_min_in_log_n(nums, mid+1, right)
        return min(left_part_min, right_part_min)


    def find_min_bi_search_way_in_log_n(self, nums: List[int], left=None, right=None) -> int:
        """
        One side should be sorted of a rotated sorted array. We can found the solution in the unsorted part.
        Based on this a sorted roted array can have 3 conditions
        - left most value < right most value - that means there is no rotationg
        - mid value > right most value -> then the min value is in the right part
        - mid value < right most value -> then the min value is in the left part

        Time complexity:
        T = T(n/2) + 1 = O(logn)
        """

        left = 0 if left is None else left
        right = len(nums)-1 if right is None else right

        # Case 1 or base case
        if nums[left] <= nums[right]:
            return nums[left]
        # Calculate the mid
        mid = left + int((right - left)/2)
        # Case 2
        if nums[mid] > nums[right]:
            return self.find_min_bi_search_way_in_log_n(nums, mid+1, right)
        # Case 3
        return self.find_min_bi_search_way_in_log_n(nums, left, mid)
```
