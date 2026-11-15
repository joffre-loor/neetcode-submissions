class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = {}
            self.times[key]["timestamps"] = []
            self.times[key]["values"] = []
        
        self.times[key]["timestamps"].append(timestamp)
        self.times[key]["values"].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        
        search = self.times[key]["timestamps"]
        values = self.times[key]["values"]

        if self.times[key]["timestamps"][0] > timestamp:
            return ""
        l,r = 0, len(search)-1

        if search[r] <= timestamp:
            return values[r]
        
        closest = -1
        index = 0
        while l <= r:
            mid = l + ((r-l) // 2)
            if timestamp > search[mid]:
                if search[mid] > closest:
                    index = mid
                    closest = search[mid]
                l = mid + 1
            elif timestamp < search[mid]:
                r = mid - 1
            else:
                return values[mid]
        
        print(closest)
        return values[index]
        
