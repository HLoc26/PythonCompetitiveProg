'''https://neetcode.io/problems/three-integer-sum'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums) - 2 and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i-1]: # Skip duplicate first num
                i+=1
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j+=1
                elif total > 0:
                    k-=1
                else:
                    found =[nums[i], nums[j], nums[k]]
                    res.append(found)
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
            i+=1
        return res