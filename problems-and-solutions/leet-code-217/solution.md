```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mark_dic = {}
        for val in nums:
            if mark_dic.get(val, None):
                return True
            mark_dic[val] = True
        return False
```
