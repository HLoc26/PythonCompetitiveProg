'''https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/'''
class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        prefix = self.prefix
    
    def prefix(self, nums: list[int]):
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[i-1] + nums[i])
        return pref