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

        # Find out the fast_head.
        for i in range(n):
            fast_head = fast_head.next

        while fast_head and fast_head.next:
            fast_head = fast_head.next
            slow_head = slow_head.next
        
        if not fast_head:
            head = slow_head.next
        else:
            slow_head.next = slow_head.next.next
        
        return head



if __name__ == "__main__":
    # Create linked list
    prev = head = None
    for item in [1, 2, 3, 4, 5]:
        temp = ListNode(item)
        if prev:
            prev.next = temp
        else:
            head = temp
        prev = temp
    head.print_list()

    s = Solution()
    res_head = s.removeNthFromEnd(head, 3)
    res_head.print_list()

