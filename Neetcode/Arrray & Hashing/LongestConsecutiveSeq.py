'''https://neetcode.io/problems/longest-consecutive-sequence'''
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if (n-1) not in numset: # Find the first num of seq
                length = 1
                while (n + length) in numset:
                    length += 1
            longest = max(longest, length)
        return longest