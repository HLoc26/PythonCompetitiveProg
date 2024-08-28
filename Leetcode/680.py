'''https://leetcode.com/problems/valid-palindrome-ii/'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Xóa ký tự từ bên trái hoặc bên phải và kiểm tra
                # Delete 1 char on left or on right to check
                deleteLeft = s[left+1:right+1]
                deleteRight = s[left:right]
                return deleteLeft == deleteLeft[::-1] or deleteRight == deleteRight[::-1]
            left += 1
            right -= 1
        return True
    
sol = Solution()
s = 'abca'
print(sol.validPalindrome(s))