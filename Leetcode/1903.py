'''https://leetcode.com/problems/largest-odd-number-in-string/'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
    
sol = Solution()
num = '3542708'
print(sol.largestOddNumber(num))