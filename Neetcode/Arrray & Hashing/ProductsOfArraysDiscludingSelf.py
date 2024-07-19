class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

sol = Solution()
nums = [3, 2, 4, 6]
nums = [3,5,2,6,7,1,2]
print(sol.productExceptSelf(nums))