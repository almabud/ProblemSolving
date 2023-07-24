# \[Leet-code] 15. Three sum

### [Problem Description](url="https://leetcode.com/problems/3sum/")

### Discussion

- The solution is pretty much simple. First sort the array.
- Fixed a number of the array and find the other value using two pointer like two sum.

### Time complexity

Here, for sorting we need `nlogn`. Outer and Inner loop iterate at max `n` times. Set addition `n`.

$=nlogn + n * (n * n (in worst case time complexity of set.add is n) ) = nlogn + n*n^2=nlogn + n^3 \cong O(n^3)$. But average case time complexity of set operation remains in `O(1)`. So, time complexity is $O(nlogn)$

```python
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
```

### Optimized Solution

```python
    def threesum_n_square(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i<len(nums):
            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue
            pointer1 = i+1
            pointer2 = len(nums) - 1
            while pointer1<pointer2:
                if nums[pointer1] + nums[pointer2] + nums[i] < 0:
                    pointer1 += 1
                elif nums[pointer1] + nums[pointer2] + nums[i] > 0:
                    pointer2 -= 1
                else:
                    res.append((nums[i], nums[pointer1], nums[pointer2]))
                    pointer1 += 1
                    pointer2 -= 1
                    # Excluding the duplicates.
                    while pointer1<pointer2 and nums[pointer1-1] == nums[pointer1]:
                        pointer1 += 1
                    while pointer1<pointer2 and nums[pointer2+1] == nums[pointer2]:
                            pointer2 -= 1
                    
            i += 1
        
        return res
```

### Time complexity

Time complexity is $O(n*2)$
