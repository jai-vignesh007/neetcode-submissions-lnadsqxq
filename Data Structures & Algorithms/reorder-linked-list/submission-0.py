# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        anotherhead=head
        array=[]
        newarr=[]
        while head is not None:
            array.append(head.val)
            head=head.next
        l=len(array)
        newarr=[None]*l
        for i in range(l):
            k=i//2
            newarr[i]=array[k] if i%2==0 else array[l-1-k]
        i=0
        for i in range(l):
            anotherhead.val=newarr[i]
            anotherhead=anotherhead.next


            

            
        
        

        
        


            
            
        