# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #reverse the linked list 1

        if l1.val==0 and l2.val==0:
            one=ListNode(0,None)
            return one
                      
        prev=None
        current=l1
        while current:
            after=current.next
            current.next=prev
            prev=current
            current=after
        
        
        prev2=None
        current2=l2
        while current2:
            after2=current2.next
            current2.next=prev2
            prev2=current2
            current2=after2

        head1=prev
        num1=0
        while head1:
            num1=num1*10+head1.val
            head1=head1.next
        head2=prev2
        num2=0
        while head2:
            num2=num2*10+head2.val
            head2=head2.next
        resultnum=num1+num2

        dummy=ListNode(0,None)
        res=dummy
        while resultnum>0:
            Unitdigit=resultnum%10
            resultnum=resultnum//10
            current=ListNode(Unitdigit,None)
            dummy.next=current
            dummy=current
            current=current.next
        
        return res.next
        
        
        


        





        