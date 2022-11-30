from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = head = None
        while list1 or list2:
            if not head:
                res_head = head = ListNode()
            if not list1 and not list2:
                break
            if list1 and not list2:
                head.val = list1.val
                head.next = list1.next
                break
            if not list1 and list2:
                print("hello")
                head.val = list2.val
                head.next = list2.next
                break
        
            if list1.val > list2.val:
                head.val = list2.val
                head.next = ListNode()
                head = head.next
                list2 = list2.next
            else:
                head.val = list1.val
                head.next = ListNode()
                head = head.next
                list1 = list1.next
        
        return res_head

            



if __name__ == "__main__":
    head = None
    for item in [1,2,4]:
        if not head:
            head_1 = head = ListNode(item)
            continue
        head.next = ListNode(item)
        head = head.next
    
    head = None
    for item in [1,3,4]:
        if not head:
            head_2 = head = ListNode(item)
            continue
        head.next = ListNode(item)
        head = head.next
    
    s = Solution()
    res_head = s.mergeTwoLists(head_1, head_2)

    while res_head:
        print(res_head.val, end=' ')
        res_head = res_head.next