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
        d={None:None}

        cur=head
        dummy=Node(0)
        res=dummy
        while cur:
            new=Node(cur.val)
            d[cur]=new
            res.next=new
            res=res.next
            cur=cur.next
        
        cur=head

        while cur:
            d[cur].random=d[cur.random]
            cur=cur.next

        return dummy.next

