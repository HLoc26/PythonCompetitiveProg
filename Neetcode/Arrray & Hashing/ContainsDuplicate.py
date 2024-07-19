class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

nums = [1, 2, 3, 3]
sol = Solution()
print(sol.hasDuplicate(nums))

'''
Input: nums = [1, 2, 3, 3]

Output: true
'''