class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq_list = list(freq.items())
        freq_list.sort(key=lambda x: x[1], reverse=True)
        top_k = [item[0] for item in freq_list[:k]]
        return top_k
    
sol = Solution()

nums = [1,2,2,3,3,3]
k = 2
print(sol.topKFrequent(nums, k))

'''
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''