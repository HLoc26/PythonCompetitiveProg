'''https://neetcode.io/problems/max-water-container'''
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = 0
        while i < j:
            water = (j - i) * min(heights[i], heights[j])
            maxWater = max(water, maxWater)
            if heights[i] < heights[j]:
                i+=1
            elif heights[i] >= heights[j]:
                j-=1
        return res
