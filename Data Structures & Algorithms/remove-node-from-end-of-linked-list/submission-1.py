# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = 0
        before = None
        current = head
        while current:
            index += 1
            current = current.next
        
        current = head
        maximum = index
        while current:
            if index == n:
                if index == maximum:
                    head = current.next
                else:
                    before.next = current.next

            before = current
            current = current.next
            index-=1
        
        return head