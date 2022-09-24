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
