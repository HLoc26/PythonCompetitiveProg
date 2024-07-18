class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        toIndex = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in toIndex:
                return [toIndex[comp], i]
            toIndex[num] = i

nums = [3, 4, 5, 6]
target = 7
sol = Solution()
print(sol.twoSum(nums, target))