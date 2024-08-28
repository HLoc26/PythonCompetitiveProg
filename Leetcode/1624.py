'''https://leetcode.com/problems/largest-substring-between-two-equal-characters/'''
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        '''
        Track the last occurance index of each char
        Then traverse from the front and check the diff of each char index with there last occurance index
        Keep tracking the max.
        '''
        last = [-1] * 26
        ans = -1
        
        for i, char in enumerate(s):
            last[ord(char) - ord('a')] = i
        
        for i, char in enumerate(s):
            ans = max(ans, last[ord(char) - ord('a')] - i - 1)
        
        return ans


sol = Solution()
s = 'abca'
print(sol.maxLengthBetweenEqualCharacters(s))