'''https://neetcode.io/problems/is-anagram'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

sol = Solution()
s = "racecar"
t = "carrace"
print(sol.isAnagram(s, t))

'''
Input: s = "racecar", t = "carrace"

Output: true
'''