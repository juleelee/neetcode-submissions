# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, l: Optional[ListNode],num :int)-> int:

            if not l : 
                return 0


            return l.val*num + self.rec(l.next,num*10)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
    



        
        num1 = [1]

        n1 = self.rec(l1,num1[0])

        num2 = [1]

        n2 = self.rec(l2,num2[0])

        somme = n1 + n2
        head = ListNode(0, next=None)
        cur = head 

        for digit in reversed(str(somme)):

            cur.next = ListNode(digit, next=None)
            cur = cur.next

        return head.next


            
            





            
            