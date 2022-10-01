```python
class Solution:
    def __init__(self):
        self.lookup_table = self._create_lookup_table()


    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(self._get_bit_count(i))
        
        return res

    def _get_bit_count(self, n: int) -> int:
        max_8_bit = 0xff

        return (
            self.lookup_table[n&max_8_bit] +
            self.lookup_table[(n>>8)&max_8_bit] +
            self.lookup_table[(n>>16)&max_8_bit] +
            self.lookup_table[(n>>24)&max_8_bit]
        )
    
    def _create_lookup_table(self) -> List[int]:
        mark_array = [0] * 256

        for i in range(1, 256):
            mark_array[i] = mark_array[i//2] + (i&1)
        
        return mark_array
```

>> The time complexity is $O(n)$ as the time complexity of finding bit ocunt is $O(1$)
