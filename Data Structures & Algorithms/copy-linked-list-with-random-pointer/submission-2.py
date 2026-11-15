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
        if not head:
            return None
        oldToNew = defaultdict()

        curr = head
        prev = None
        while curr:
            oldToNew[curr] = Node(curr.val)
            if prev:
                prev.next = oldToNew[curr]
            prev = oldToNew[curr]
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        
        return oldToNew[head]