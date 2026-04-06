# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        res=dummy
        fast=head

        for _ in range(n):
            fast=fast.next

        while fast:
            dummy=dummy.next
            fast=fast.next
        dummy.next=dummy.next.next
        return res.next


        