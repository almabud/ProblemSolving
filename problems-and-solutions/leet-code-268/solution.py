from typing import List
from functools import reduce


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_xor = reduce(lambda x, y: x^y, range(len(nums)+1))
        nums_xor = reduce(lambda x, y: x^y, nums)

        return all_xor ^ nums_xor


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,8,1]))