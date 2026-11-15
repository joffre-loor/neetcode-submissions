# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode(0)
        dummy.next = lists[0]
        for i in range(1, len(lists)):
            main = dummy
            l2 = lists[i]
            while main.next and l2:
                if l2.val <= main.next.val:
                    next = l2.next
                    l2.next = main.next
                    main.next = l2
                    l2 = next
                    main = main.next
                else:
                    main = main.next
            
            if l2:
                main.next = l2
        

        return dummy.next
            
            