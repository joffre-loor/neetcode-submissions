
class Node:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        count = 0
        ptr = self.head.next
        while ptr and count < index:
            ptr = ptr.next
            count+=1

        if ptr == None:
            return -1

        return ptr.val

    def insertHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val)
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        count = 0
        ptr = self.head
        while ptr and count < index:
            ptr = ptr.next
            count+=1

        if ptr and ptr.next:
            if ptr.next == self.tail:
                self.tail = ptr
            ptr.next = ptr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        arr = []
        ptr = self.head.next
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        return arr
