'''https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        # Tìm các chỉ số khác nhau giữa s1 và s2
        diff_indices = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_indices.append(i)
                if len(diff_indices) > 4:
                    return False
        
        # Nếu có chính xác 2 vị trí khác nhau, kiểm tra điều kiện hoán đổi
        if len(diff_indices) == 2:
            i, j = diff_indices
            return s1[i] == s2[j] and s1[j] == s2[i]

        return False

sol = Solution()
s1 = 'bank'
s2 = 'kanb'
print(sol.areAlmostEqual(s1, s2))