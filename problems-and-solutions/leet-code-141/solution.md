# [Leet-code-141] Linked List Cycle

### Discussion:

This is solve by **Floyd’s Cycle Finding Algorithm**.

* Concept is to use **two pointer**.
* Both pointer start from same position but one pointer should move by **1** and another should move by **2** step.

### Implementation:

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.hare_tortoise_algo(head)

    def hare_tortoise_algo(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast:
            if not fast.next or not fast.next.next:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next
        
        return False
```

### Time complexity:

Here we need visit all nodes for the worst case so the time complexity is $O(n)$

### Space complexity:

We didnt' use any extra space so space complexity is $o(1)$

### Reference:

* [Floyd’s Cycle Finding Algorithm](https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/#:~:text=Floyd's%20cycle%20finding%20algorithm%20or,fast%20as%20the%20other%20one.)
