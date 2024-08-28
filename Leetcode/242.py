'''https://leetcode.com/problems/valid-anagram/'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = dict()
        if len(s) != len(t):
            return False
        
        # Decrement the frequency of characters in string t
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        print(count)
        
        return True

sol = Solution()
s = 'anagram'
t = 'nagaram'
print(sol.isAnagram(s, t))