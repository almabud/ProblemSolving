# [Leet-code] 242.  [ Valid Anagram]("https://leetcode.com/problems/valid-anagram/")

## Solution Approach

### Approach 1:

- If lenght is not same then it can't be a anagram. So, 1st step to check that the lengh is same or not and return false if not same.
- Here, you can see that if the both string charecter count is equal then it will be a valid anagram.
- We will use `two` mark array for storing the charecter count. As, we will use the aschi code of the charecter as the index of array. So, the array size should be `0 < array_size <= 256`.
- At last we will loop through the mark array and compair the values of each index. If any index value is not equal then return `False`.

### Approach 2:

- We can sort the both string and then check the two string is equal or not.

## Implementation

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.bit_solv(s, t)
    
    def mark_array_sol(self, s: str, t: str) -> bool:
        # Len is not same then it is not a valid anagram.
        if len(s) != len(t):
            return False
        
        # Initialize mark array
        mark_arr1 = [0] * 256
        mark_arr2 = [0] * 256
        
        for key, val in enumerate(s):
            mark_arr1[ord(val)] += 1
            mark_arr2[ord(t[key])] += 1
        
        for key, val in enumerate(mark_arr1):
            if val != mark_arr2[key]:
                return False
        
        return True


    def sort_solv(self, s: str, t: str) -> bool:
        # Len is not same then it is not a valid anagram.
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
```

## Time & Space Complexity:

- The time coplexity for mark array approach. You can see from the solution we only running two loops at most n times. 

  - $= n + n = 2n \approx O(n)$
  - Sapce Complexity. We used 2 mark array and the size is 256 and and for two string the size is s and t.
  - $=O(s+t)$

- The time complexity of sorting approach. we know for sorting time complexity is $nlog(n)$.
  - $slog(s)$ as the lenght is same because we check the lenght at the beggining.
