'''https://neetcode.io/problems/trapping-rain-water'''
# TBH, I don't know how to solve this problem, so I watch the solution, and I can't understand it either :(
class Solution:
    def trap(self, height: list[int]) -> int:
        # Using 2 pointer i and j
        i = 0
        j = len(height) - 1
        max_i = height[i] # Get the max height on the left
        max_j = height[j] # Get the max height on the right
        res = 0
        '''
        Traverse from left (i) and right (j). The condition to move pointer is if its height is lower than the other pointer.
        On every move, if the height at the new move index is higher than max_i (or max_j, depends), it means that index can't hold water.
        Otherwise, the water it can hold is max_i (or max j, depends) - height[index] 
        '''
        while i < j:
            if max_i < max_j:
                i+=1
                max_i = max(max_i, height[i])
                res += max_i - height[i]
            else:
                j-=1
                max_j = max(max_j, height[j])
                res += max_j - height[j]
        return res

sol = Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(height))