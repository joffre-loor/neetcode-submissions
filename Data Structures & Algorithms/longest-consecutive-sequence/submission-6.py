class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        longest = 1
        last = None
        currentNum = heapq.heappop(nums)
        current = 1
        while nums != []:
            last = currentNum
            currentNum = heapq.heappop(nums)
            print(f"last: {last}, current:{currentNum}, seqlen: {current}")
            if last == currentNum:
                continue
            elif last+1==currentNum:
                current+=1
                if current > longest:
                    longest = current
            else:
                current = 1
        
        return longest
            