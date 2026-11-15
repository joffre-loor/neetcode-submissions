class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        arr = self.tm[key]
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + ((r-l) // 2)
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            
            if arr[mid][0] < timestamp:
                res = arr[mid][1]
                l = mid+1
            else:
                r = mid-1

        return res
        
