'''https://leetcode.com/problems/buddy-strings/'''
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            return len(set(s)) < len(s)
        s = list(goal)
        goal = list(goal)
        n = len(s)
        i, j = 0, n-1
        while i < n and s[i] == goal[i]:
            i+=1
        while j > 0 and s[j] == goal[j]:
            j-=1

        if i < j:
            s[i], s[j] = s[j], s[i]
        return s == goal

sol = Solution()
s = 'ab'
goal = 'ba'
print(sol.buddyStrings(s, goal))