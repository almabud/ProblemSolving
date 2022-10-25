from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



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
            

if __name__ == "__main__":
    s = Solution()
    list_head = [1,2,3,4,5,6]
    heads:[ListNode] = []
    head = prev_head = ListNode(list_head[0])
    for i in range(1, len(list_head)):
        cur = ListNode(list_head[i])
        if prev_head:
            prev_head.next = cur
        prev_head = cur
    
    head = s.reverseList(head)

    while head:
        print(head.val, end=" ")
        head = head.next