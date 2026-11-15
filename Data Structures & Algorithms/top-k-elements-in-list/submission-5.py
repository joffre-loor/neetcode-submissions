class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums) + 1)]

        count = defaultdict(int)

        for num in nums:
            count[num] +=1
        
        for num in count.keys():
            frequency[count[num]].append(num)

        print(frequency)
        res = []
        for i in range(len(frequency)-1, 0, -1):
            for num in frequency[i]:
                if len(res) == k:
                    break
                res.append(num)

        return res