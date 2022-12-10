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




if __name__ == "__main__":
    # Create linked list
    prev = head = None
    for item in []:
        temp = ListNode(item)
        if prev:
            prev.next = temp
        else:
            head = temp
        prev = temp
    head.print_list()

    s = Solution()
    s.reorderList(head)
    head.print_list()

