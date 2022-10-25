# [Leet-code-206] Reverse linked list

### Implementation:

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       return self.recursive_reverse(head)

    def iterative_reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        
        return prev
    
    def recursive_reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case.
        if not head or not head.next:
            return head
        
        prev = head
        cur = head.next
        reverse_head = self.recursive_reverse(head.next)
        cur.next = prev
        prev.next = None
        
        return reverse_head
```

### Time complexity:

Time complexity is $O(n)$ as we need to visit the all nodes.
