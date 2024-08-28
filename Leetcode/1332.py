'''https://leetcode.com/problems/remove-palindromic-subsequences/'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2
    
# If s is not palindrome, we can delete all a's, and then delete all b's --> 2 steps
# Else, delete the whole string --> 1 step

sol = Solution()
s = 'baaba'
print(sol.removePalindromeSub(s))