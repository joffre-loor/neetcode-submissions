# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        current = head
        while current.next:
            nextNode = current.next
            print(nextNode)
            if nextNode.val < current.val or nextNode.val == current.val:
                return True
            current = nextNode
        return False