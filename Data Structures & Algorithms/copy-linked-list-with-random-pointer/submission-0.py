"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        
        hash_copy = {None: None}

        cur = head 
        while cur : 
            copy = Node(cur.val)
            hash_copy[cur] = copy 
            cur = cur.next
        
        cur = head 

        while cur : 
            copy = hash_copy[cur]
            copy.next = hash_copy[cur.next]
            copy.random = hash_copy[cur.random]

            cur = cur.next 
        
        return hash_copy[head] 


        