## Discussion:

We know that in a sequence from `0` to `n`. 

$$
a_n = a_1 \oplus a_2 \oplus a_3 \oplus ... \oplus a_n \\

a_{(n-1)} = a_1 \oplus a_2 \oplus a_3 \oplus ... \oplus a_{(n-1)} \\

missing\_value = a_n \oplus a_{(n-1)}
$$

```python

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_xor = reduce(lambda x, y: x^y, range(len(nums)+1))
        nums_xor = reduce(lambda x, y: x^y, nums)

        return all_xor ^ nums_xor
```
