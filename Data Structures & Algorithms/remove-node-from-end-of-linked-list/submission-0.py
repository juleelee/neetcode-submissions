# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        first = head 

        second = head
        # sliding window size
        for i in range(1,n+1): 
            second = second.next 
        
        if not second : 
            return head.next

        print(first.val,second.val)
        while second.next : 
            first = first.next 
            second = second.next
        
        tmp = first.next.next 

        first.next = tmp 

        return head 




        
