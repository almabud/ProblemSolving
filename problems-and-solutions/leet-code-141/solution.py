from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next_head=None):
        self.val = x
        self.next = next_head

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



if __name__ == "__main__":
    s = Solution()
    list_head = [1,2,3,4,5,6]
    heads:[ListNode] = []
    head = prev_head = ListNode(list_head[0])
    # for i in range(1, len(list_head)):
    #     cur = ListNode(list_head[i])
    #     if prev_head:
    #         prev_head.next = cur
    #     prev_head = cur

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head
    print(s.hasCycle(head))