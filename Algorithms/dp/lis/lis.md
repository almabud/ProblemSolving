# Longest Increasing Subsequence (LIS)

[Substring, Subsequence](../lcs/lcs.md)

The longest increasing subsequence mean the longest subsequence whice are sorted in increasing order.

eg. $\{10, 22, 9, 33, 21, 50, 41, 60, 80\}$. Here total subsequence is $2^n$. But longest increasing subsequence is
$\{10, 22, 33, 41, 60, 80\}$ and the length is `6`.

### Recursive Solution:

* We start from index `i` and index `j=i+1`. Now we will take the $j_{th}$ postion $if \  i < j < n \ \\& \  seq[j] > seq[i]$. where sequence will start
from index `i`.
* We need to calculate lis for every position. Above condition is for one position.
* So, we ca find the **LIS** of $f(10), f(22), f(9), ... f(n-1)$ and we will pick the maximum from this **LIS** . $max(f(10), f(22), f(9), ... f(n-1))$.

> This solution time complexity is $n^2$.

### Implementation:

```python
class LIS:
    def find_LIS(self, seq: List[int]) -> int:
        return self.find_recursive_LIS_v1(seq)
    
    def find_recursive_LIS_v1(self, seq: List[int]) -> int:
        """
            Find the LIS for every position.
        """

        ans = 0
        dp = [-1] * len(seq)
        for i, val in enumerate(seq):
            ans = max(ans, self.recursive_dp_LIS_v1(seq, i, dp))
        
        return ans
    
    def recursive_dp_LIS_v1(self, seq: List[int], index: int, dp: List[int]) -> int:
        if dp[index] != -1:
            return dp[index]
        # Declare the res with inital value.
        ans = 0
        for j in range(index+1, len(seq)):
            if seq[j] > seq[index]:
                ans =  max(ans, self.recursive_dp_LIS_v1(seq, j, dp))

        # Add the 1st value  for the starting point.
        dp[index] = ans + 1

        return dp[index]
```

### Time complexity:

For every state `n` times loop is running. so for `n` state time complexity $O(n*n)$

> This is for dp solution for reqursive solution it will be $2^n$ exponential.

### Iterative Solution:

* We will manage a array `d[]`.
* We will traverse the `seq` and update the `d`.
  * We will traverse through the `d` for a `seq[i]` and update the `d` if `seq[i]` has position in `d`. The position will be
  calculated for the increasing order and maintain the `seq` original order. So, We have just 2 operations.
    * We can replace the value of `d[j]` if `seq[i]` is less than `d[j]`.
    * Add new value in the `d[j]` if `seq[i]` is greater than the all value of `d`.
    
    > We can't add value in the middle of the `d` or start of the `d`. Because it will break the original order of `seq`. Thus we can't
    get the **LIS**. So we can just add value at the end of the `d`. We, will replce the value if $seq[i] < d[j]$ cause it will create
    possibility to find largest sequence. We can get largest sequence if we take possible lowest value from left to right.

    eg. `d=[4,5,6]`. Now for `seq[i]=3`. `3` has the position in `d[0]=4` we will replace by `d[0]=3`. `seq[i]=7` has the position
    at the end of the `d`. So the `d=[3,5,6,7]`. This way we will update the `d` with increasing order. It means every new lowest value
    is the new start of a sequence.
  * By doing this we will get a largest subsequence after the iteration. And the length of `d` will be the length of **LIS**.

### Simulation:

```
    seq = [4,10,4,3,8,9]
    d = []

    step-1: For seq[0] = 4. The d is empty so we will add 4.
            New d = [4]
    
    step-2: For seq[1] = 10. The position of 10 is after 4 or d[0].
            New d = [4, 10]
    
    step-3: For seq[2] = 4. There is no any suitable position for 4 in d.
            d = [4, 10]
    
    step-4: For seq[3] = 3. The suitable position is before 4 in d. But we can't 
            add it before 4 as  it will break the seq order. We will replace this 
            by 3 as 3 is less than 4. So, that if there is any seq that is greter 
            than 3 we can adapt it like 4.
            new d = [3,10]
    
    setp-5: For seq[4] = 8. The suitable position for 8 is before 10 and after 3 in d. 
            But we can't add it to here as the order of seq will be break. As 8 is less 
            than 10 so we will replace this 10 with 8. Because we can have bigger sequence 
            if we take the lowest value.
            new d = [3,8]
    
    step-6: For seq[5] = 9. The suitable position for 9 is after 8 which is at the end of 
            the d. See, if we take the 10 before then we miss this 9. For chosing 
            the 8 we can get the largest sequence.
            new d = [3,6,9]
    
    So, The LIS length is 3.
    Here main thing is to replace the seq[i] if it is less than any value of d[j] and 
    add seq[i] to d[j] if it is greater than the all value of d.
        
```

### Implementation:

```python
class LIS:
    def LIS_n_square(self, seq: List[int]):
        max_int = 999999
        min_int = -999999

        # Initialize the d
        d = [max_int] * (len(seq) + 1)
        d[0] = min_int

        for seq_val in seq:
            # Finding the suitable position for seq_val
            for j in range(1, len(d)):
                if d[j-1] < seq_val < d[j]:
                    d[j] = seq_val
        
        lis = 0
        for index, val in enumerate(d):
            if val < max_int:
                lis = index
        
        return lis
```

> Here, you can see `d` always be sorted. So, we can find the suitable position for `seq[i]` by $log(n)$.

### Time complexity:

Here,  `3` loops is running upto `n`. Two of them are nested. Other statements are conostant. So, the time complexity is $n+n*n = n+n^2=O(n^2)$.

### Optimization:

```python
class LIS:
    def LIS_n_log_n(self, seq: List[int]):
        max_int = 999999
        min_int = -999999

        # Initialize the d
        d = [max_int] * (len(seq) + 1)
        d[0] = min_int

        def find_the_suitable_position(key: int) -> int:
            left = 0
            right = len(d) - 1
            
            while(right-left>1):
                mid = left + (right-left) // 2

                if key <= d[mid] <= max_int:
                    right = mid
                else:
                    left = mid
            
            return right

        for seq_val in seq:
            # Finding the suitable position for seq_val
            d[find_the_suitable_position(seq_val)] = seq_val
        
        lis = 0
        for index, val in enumerate(d):
            if val < max_int:
                lis = index
        return lis
```

### Time complexity:

Here, `3` loops is running upto `n`. Two of them are nested but nested loop time complexity is $log(n)$ as this is binary search. Other statements are conostant. So, the time complexity is $n+n*log(n) = n+nlog(n)=O(nlog(n))$.

### Space complexity:

We used a separate array size of $n+1$. So, space complexity is $O(n)$

> [Source code](lis.py)

### Reference:

* http://www.shafaetsplanet.com/?p=1211
* https://cp-algorithms.com/sequences/longest_increasing_subsequence.html#restoring-the-subsequence
* https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
