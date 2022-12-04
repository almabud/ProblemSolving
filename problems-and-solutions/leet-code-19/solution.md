# [Leet-code-19] Remove Nth Node From End of List.

### Discussion:

* The idea is to take 2 pointer. slow pointer should start from 0 and fast pointer should start from the $n_{th}$ position.
* Now start the visiting the node. The slow pointer will go to the $n_{th}$ position from the `end` while the fast pointer reached to
the  end of the list.

### Example: 

for [1] -> [2] -> [3] -> [4] -> [5] -> None remove the $2_{nd}$ position from the end.
* The fast pointer should start from $2_{nd}$ postion from the beginning.
* The slow pointer should start from $1_{st}$ postion from the begining.
* Now start iterating until the `fast_pointer.next` is `None` mean the last val. 
`fast_pointer = 2` and `slow_pointer = 1`. 
  * 1st iteration: `fast_pointer = 3` and `slow_pointer = 2`.
  * 2nd iteration: `fast_pointer = 4` and `slow_pointer = 3`.
  * 3rd iteration: `fast_pointer = 5` and `slow_pointer = 4`.

  > So here we need remove the `slow_pointer position` that is `4`.

Here, if the `slow_pointer` reached to the `3` then we can just do this -> 
`slow_pointer_node.next = slow_pointer_node.next.next` and the position `4` will be removed. 
So, We need to stop the iteraion earlier. 

We, could do that if we keep the fast pointer ahead by 1 than the actual position. That means
we need to start the `fast pointer` from `n+1`. In this case from `[3]`.

Another problem, what about the head. I mean need to remove the head. In this case we want to remove the
$5_{th}$ position from the end which is `1`. 

In that case you can see `fast pointer` will be `None` rather than the last value. For other case it is just the `last value`.

* eg. `fast_pointer = None` and `slow_pointer = 1`. so, there will be no iteration as `fast pointer` already in the last.

So, If `fast_ponter` is None then we need to remove the head.

### Implementaion:

```python
from typing import Optional


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def print_list(self, head=None):
        head = self if not head else head
        # Print Linked list
        while head:
            print(head.val, end=' ')
            head = head.next
        print()


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_head = fast_head = head

        # Find out the fast_pointer.
        for i in range(n):
            fast_head = fast_head.next

        while fast_head and fast_head.next:
            fast_head = fast_head.next
            slow_head = slow_head.next
        
        if not fast_head:
            # Need to remove the head.
            head = slow_head.next
        else:
            slow_head.next = slow_head.next.next
        
        return head
```

### Time Complexity:

$= n + n = 2n \approx n \approx O(n)$

### Space Complexity:

Here, we didn't use extra space so space complexity is $O(1)$
