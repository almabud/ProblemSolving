### Discussion

We can solve this problem in many ways.

#### Naive approach:

* Right shift the number until it turn to `0`.

* Then each time check the right most value is set or not.

* If set then count the value.

* The time complexity of this approach will be $\textbf{log(n)}$

#### Karnighan Algorithm:

* We can solve this using Karnighan Algorithm.

* The idea behind this algorithm is to check the first set bit from right side count it and unset it.

* Here we will consider the only set bits. So, We don't need to loop through all the `32` bits like naive approach.

* How we unset the right most set bit? $\textbf{(x \\& (x-1))}$ by this we can unset rightmost set bit.

* We will run the above formula untile the number turns to `0`. That means until the set bit are unset.

* This is faster than naive approach as it will iterate through the set bit only. But in worst case the 
time complexity will be $\textbf{O(logn)}$

### Using Lookup table:

* We can use a loopkup table. This solution is seems to me little bit complex and can't find satisfying explanation.
So, I'm explaining my thoughts.

* Here we will store the bit count of every possible number and store it in a `mark` array where mark array index will be
the **value** whose bit count is stored. Now, if we try to store `32` bit integer then the we need the array size $2^32 = 4294967296$.
As this is a `32` bit unsigned integer. This is huge and we can't afford this index.

* So, We can brek a 32 bit number into many slices. Like we can break this number into `4` pieces which will be `8` bit number.

* Process and count the `8` bit number then right shift it by `i*8` where i start from `1`. Thus the process bit will be removed
for the right shifting and then we can process next `8` bit.  Atlast we can sum the all process bit to get the output.

* Now question is How we will store this value? We can store the bitcount by naive approach but that is not worthy as because it
will loop through the all bits though. Thus we can't improve the performance. We can matmatically count the bit in an efficient way.
Let's see this.

  * For `0` the bit count will be `0`. So, we set the `mark_array[0] = 0` as the bit count is 0.
  * For `1 = 00000001` here count is `1`.
    *  We left shift this by `1`. $00000001 << 1 = 00000010 = 2$ which is $count\_of(000000001) + last\_bit(00000010) = 1$

    * We again left shift the value by `1`. $00000010 << 1 = 00000100 = 4$ $ which is $count\_of(000000010) + last\_bit(00000100) = 1$

    * Left shift again. $00000100 << 1 = 00001000 = 8$ $ which is $count\_of(000000100) + last\_bit(00001000) = 1$

    * We can use the prvious counting value and this is happening as $x << 1 = 2.x$ and $x >> 1 = \dfrac{x}{2}$. But why we count consider
      last bit? Lets simulat it by `1, 2, 3, 4..`
    
    * We see that for `1, 2, 4, 8` respectively `mark_array[1] = 1, mark_array[2] = 1, mark_array[4] = 1, mark_array[8] = 1`. That means all power of 2's bit count will be `1`.

    * For `3 = 00000011` bit count is 2. How we can derived it. If we left shift `1` then the `1 = 00000010`. You can see that `3` is nothing but set the right most bit of `1's` left shift. We've already count the `1's` bit. We just need the last bit count. We can get the right most bit by doing `&` with the value. So, the result is $bit\_count(3=00000011) = mark\_array[1] + last\_bit\_of(3)$.

    * For `5 = 00000101`. So, the result is $bit\_count(5=00000101) = mark\_array[2] + last\_bit\_of(5) = 1 + 1 = 2$.
    It will work as same for the rest of numbers.

    * What is happening if we right shift the value by `1` then we can see the value's bit is already counted we just need considar the last bit.
    Right shift means $x >> 1 = \dfrac{x}{2}$. By this way we can count the every numbers set bit without lopping through the ever number all bit.


```python

class Solution:
    def __init__():
        self.mark_array = self.create_lookup_table()
    
    def hammingWeight(self, n: int) -> int:
        return self.look_up_table(n)

    def naive_solution(self, n: int) -> int:
        n = int(n, 2)
        count_set_bit = 0
        while n:
            if n & 1:
                count_set_bit += 1
            n >>= 1

        return count_set_bit
    
    def karnighan_algorithm(self, n: int) -> int:
        """
        Idea is to unset the set bit from the right side. 
        We can do this by `x & (x-1)` and count each time.
        """

        bit_set_count = 0
        while n:
            n = n & (n-1)
            bit_set_count += 1
        
        return bit_set_count
    
    def look_up_table(self, n: int) -> int:
        # The mark aray is devide by 8 bit.
        # 8 bit max number
        max_8_bit = 0xff
        res = (
            self.mark_array[n&max_8_bit] # 8 bit
            + self.mark_array[(n>>8)&max_8_bit] # next 8 bit
            + self.mark_array[(n>>16)&max_8_bit] # next 8 bit
            + self.mark_array[(n>>24)&max_8_bit] # last 8 bit
        )
        return res

    def create_lookup_table(self) -> List:
        # Unsigned 8 bit number can sotore upto 2**(8-1) = 256.
        mark_array = [0] * 256
        # binary 0 have no set bit.
        mark_array[0] = 0
        # Don't need to calculate 0's count as we get that already.
        for i in range(1,256):
            # Right shift the i and we can see that this value is already counted. So no need to count this again.
            # Right shift i means i>>1 = i/2
            # We just need the last bit count.
            mark_array[i] = mark_array[i//2] + (i&1)
        
        return mark_array
```
