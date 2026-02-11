# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        oddhead=head
        evenhead=head.next
        op=oddhead
        ep=evenhead
        

        while op and ep:
            op.next=op.next.next
            op=op.next
            ep.next=ep.next.next
            ep=ep.next

        op.next=evenhead
        return head


        