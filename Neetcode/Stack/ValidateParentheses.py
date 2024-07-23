'''https://neetcode.io/problems/validate-parentheses'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(','{','[']
        close = [')','}',']']
        for parentheses in s:
            if parentheses in open:
                stack.append(parentheses)
            else:
                if len(stack) == 0 or open.index(stack[-1]) != close.index(parentheses):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

sol = Solution()
s = "]"
print(sol.isValid(s) == False)