'''https://neetcode.io/problems/anagram-groups'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        for string in strs:
            key = tuple(sorted(string))
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        return list(groups.values())

strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))

'''
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
