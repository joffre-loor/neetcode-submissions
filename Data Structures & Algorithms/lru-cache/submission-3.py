class Node:
    def __init__(self, key=0, val=0):
        self.next = None
        self.prev = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict()
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
    
    def insert(self, node):
        prev, next = self.left, self.left.next
        node.prev = self.left
        node.next = next
        self.left.next = node
        next.prev = node

    def remove(self, node):
        prev, next = node.prev, node.next
        next.prev = prev
        prev.next = next

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key=key, val=value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
