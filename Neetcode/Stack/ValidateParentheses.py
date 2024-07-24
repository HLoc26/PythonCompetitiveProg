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

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        stack = []
        for char in s:
            # Nếu char là dấu ngoặc mở
            if char not in brackets:
                stack.append(char)
                continue
            # Nếu char là dấu ngoặc đóng
            if len(stack) == 0 or stack[-1] != brackets[char]:
                return False
            stack.pop()
        return len(stack) == 0
