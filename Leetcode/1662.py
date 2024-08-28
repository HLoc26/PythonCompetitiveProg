class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
    

sol = Solution()
word1 = ['ab', 'c']
word2 = ['a', 'bc']
print(sol.arrayStringsAreEqual(word1, word2))