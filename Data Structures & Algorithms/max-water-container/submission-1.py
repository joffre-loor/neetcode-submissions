class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = -1

        l, r = 0, len(heights)-1

        while l < r:
            firstHeight = heights[l]
            secondHeight = heights[r]

            minHeight = min(firstHeight, secondHeight)
            width = r - l

            maxWater = max(width * minHeight, maxWater)

            if firstHeight < secondHeight:
                l+=1
            else:
                r-=1
        
        return maxWater