class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.cache:

            del self.lru[key]
            self.lru[key] = {}
            return self.cache[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        if key in self.lru:
            del(self.lru[key])
        self.lru[key] = {}

        if len(self.lru) > self.capacity:
            first_key = next(iter(self.lru))
            del self.lru[first_key]
            del self.cache[first_key]
