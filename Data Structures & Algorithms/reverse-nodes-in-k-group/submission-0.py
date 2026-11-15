# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ref = head
        num_groups = 0
        dummy = ListNode(0, head)
        prevGroup = dummy

        def findKth(node, count):
            while node and count != 0:
                node = node.next
                count-=1
            return node

        while True:
            nextNode = findKth(prevGroup, k)
            if not nextNode:
                break

            nextGroup = nextNode.next
            prev = nextGroup
            curr = prevGroup.next
            count = k

            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevGroup.next
            prevGroup.next = nextNode
            prevGroup = tmp

        return dummy.next