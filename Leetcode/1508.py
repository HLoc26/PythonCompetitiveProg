'''https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/'''
class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        subArr_sum = []

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                subArr_sum.append(curSum)
        
        subArr_sum.sort()
        mod = 10**9 + 7

        res = sum(subArr_sum[left-1 : right]) % mod
        return res