## Discussion:

We will solve this using two pointer approach.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_point = 0
        right_point = len(s) - 1 
        while left_point <= right_point:
            if not s[left_point].isalnum() and not s[right_point].isalnum():
                left_point += 1
                right_point -= 1
                continue
            elif not s[left_point].isalnum():
                left_point += 1
                continue
            elif not s[right_point].isalnum():
                right_point -= 1
                continue
            
            if s[left_point].lower() != s[right_point].lower():
                return False
            
            left_point += 1
            right_point -= 1
        
        return True
```
