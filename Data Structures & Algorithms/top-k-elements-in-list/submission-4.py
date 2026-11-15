class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1
        
        arr = [[] for _ in range(len(nums)+1)]
        for key, item in hashmap.items():
            arr[item].append(key)
        
        top = []
        arr.reverse()
        for element in arr:
            while len(element) != 0 and len(top) < k:
                top.append(element.pop())
        
        return top
        