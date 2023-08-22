# [Leet-code] 1. [Two sum](url="https://leetcode.com/problems/two-sum/")

### Discussion

We can solve this problem in two ways.
- Using hash map
- Using two pointer

### HashMap

- 1st we will insert the all list data in a dictionary. Where value will be key and the index will be value.
- It will remove all duplicate data. As we jus need one pair of solution it's okay to remove the duplicates.
  Eg. `[1,2,3,3,4]` for this dict will be `{1: 0, 2:1, 3:3, 4:4}`. Here duplicate value is removed.
- Now, we will trverse through the number and check `target-val` is present in the dict or not. 
- If the value is found in the dict will make it a pair and stop the loop.

### Time Complexity

Time complexity is $O(n)$ as we just use a loop only.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_store = {value:key for key, value in enumerate(nums)}
        for key, val in enumerate(nums):
            search_val = target - val
            if dict_store.get(search_val) and key != dict_store.get(search_val):
                res = (key, dict_store.get(search_val))
                break
                
        return res
```

### Using two pointer

- First we will sort the array.
- But we need to return the original index. So, We need to store the index. So, create list of pair with (index, value) and then sort it.
- Now created a two pointer where both bointer initial value weill be respectively `0,n-1`
- The pointers movement part. eg. `[2, 3, 4]` here target is `7`.
   - `7 - 2 = 5`. Here we need to search `5`. The 2nd pointer is definately the largest value in the list. So, we can say that `4<5`. That mean we need more larger value. So we should move the `pointer1` as in the next value will be larger.
   - So, if `target - value of pointer1 >= value of pointer2` then we will move the `pointer1` other wise we will move `pointer2`

### Time complexity

Here we sort the array which timecomplexity is $nlogn + n \cong O(n)$

```python
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
```
