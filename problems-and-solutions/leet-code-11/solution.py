from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.solution_in_n(height)

    def solution_in_n(self, height: List[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = -999999
        while left_pointer < right_pointer:
            # Calculate the area
            if height[left_pointer] >= height[right_pointer]:
                area = (right_pointer-left_pointer) * height[right_pointer]
                right_pointer -= 1
            else:
                area = (right_pointer-left_pointer) * height[left_pointer]
                left_pointer += 1
            max_area = max(max_area, area)
        
        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,1]))

