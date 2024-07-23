'''https://neetcode.io/problems/two-integer-sum-ii'''
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            total = numbers[i] + numbers[j]
            if total > target:
                j-=1
            elif total < target:
                i+=1
            else:
                return [i+1, j+1]
        