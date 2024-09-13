# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        c=head
        while c:
            next=c.next
            c.next=dummy.next
            dummy.next=c
            c=next
        return dummy.next   
        
