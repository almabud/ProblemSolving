# [Leet-code-143] Reorder List

### Discussion:

For `1->2->3->4->5` make it `1->5->2->4->3`.

* Here, the first half is `1->2->3` and last half is `4->5`.
* Now observe the result you can see that last half is reverse order. `..->5->...->4`
* So, We could devide the list by 2.
* Reverse the right part. `5->4`
* Then loop thorough the left half and merging the list accordingly. eg. `1->5->2->4->3`

### Implementation:

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the midle.
        mid_head = fast_head = head

        while fast_head and fast_head.next:
            mid_head = mid_head.next
            fast_head = fast_head.next.next
        
        rev_head = self.reverse_linked_list(mid_head)
    
        cur_head = head
        while cur_head != rev_head:
            cur_next = cur_head.next
            cur_head.next = rev_head
            cur_head = rev_head
            rev_head = cur_next
    
    def reverse_linked_list(self, head):
         head = head
         prev = None

         while head:
            head_next = head.next
            head.next = prev
            prev = head
            head = head_next

         return prev
```


### Time Complexity:

Here, We used two loop one is run up to $\dfrac{n}{2}$ and another also run up to $\dfrac{n}{2}$. So, time complexity is 
$=\dfrac{n}{2} + \dfrac{n}{2} = n = O(n)$
