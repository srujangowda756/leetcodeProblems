# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        prev=None
        cur = node
        while cur:
            front=cur.next
            cur.next=prev
            prev=cur
            cur=front
        return prev

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow=cur=fast= head

        while fast and fast.next:
            slow=slow.next
            fast= fast.next.next

        second_half=self.reverse(slow.next)

        slow.next=None

        while second_half:
            front1=cur.next
            front2=second_half.next
            cur.next=second_half
            
            second_half.next=front1

            cur=front1
            second_half=front2


