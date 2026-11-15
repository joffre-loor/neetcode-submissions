# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        if head.next is None:
            return head

        current = head.next
        before = head
        before.next = None
        while current != None:
            nextNode = current.next
            
            current.next = before
            before = current
            current = nextNode

        return before