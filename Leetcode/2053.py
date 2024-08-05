'''https://leetcode.com/problems/kth-distinct-string-in-an-array/description/'''
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        res = [key for key in freq.keys() if freq[key] == 1]
        '''
        res = []
        for key, value in freq.items():
            if value == 1:
                res.append(key)
        '''
        if len(res) < k:
            return ""
        return res[k-1]
    
    def kthDistinct2(self, arr: list[str], k: int) -> str:
        from collections import Counter
        count = Counter(arr)
        distinct = [string for string in count if count[string] == 1]
        if len (distinct) < k:
            return ""
        return distinct[k-1]

arr = ["d","b","c","b","c","a"]
k = 3
sol = Solution()
print(sol.kthDistinct(arr, k))