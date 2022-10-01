## Discussion:

* Create an empty binary which is `0`.

* left shift the empty binary by `1` and find the right most bit by `num & 1`. then fit this to res last bit by using `|`.

* Every time we left shift the result and right shift the `n`. left shift the result for make an space to set the new bit.
Right shift the `n` to remove the last bit.

* Do this until n turns into `0`.


```python
class Solution:
    def reverseBits(self, n: int) -> int:
        return self.reverse_naive_solution(n)

    def reverse_naive_solution(self, n: int) -> int:
        max_32_bit = 0xffffffff
        res = 0

        for i in range(32):
            res = ((res<<1) | ((n>>i)&1)) & max_32_bit
            print(bin(res))
        
        return res
```
