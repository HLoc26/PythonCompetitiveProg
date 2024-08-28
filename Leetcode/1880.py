'''https://leetcode.com/problems/check-if-word-equals-summation-of-two-words'''

class Solution:
    def sum(self, word: str) -> int:
        num = 0
        for char in word:
            digit = ord(char) - ord('a')
            num = num * 10 + digit
        return num
    
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.sum(firstWord) + self.sum(secondWord) == self.sum(targetWord)
    
sol = Solution()
firstWord = 'acb'
secondWord = 'cba'
targetWord = 'cdb'
print(sol.isSumEqual(firstWord, secondWord, targetWord))
