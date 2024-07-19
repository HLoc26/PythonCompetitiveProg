
# WARNING: Bad code
# class Solution:
#     def encode(self, strs: list[str]) -> str:
#         if len(strs) == 0:
#             return "0"
#         if len(strs) == 1 and len(strs[0]) == 0:
#             return "1"
#         return "à".join(strs).rstrip("à")
#     def decode(self, s: str) -> list[str]:
#         if s == "0":
#             return []
#         if s == "1":
#             return [""]
#         return s.split("à")
    
# sol = Solution()
# strs = ["neet","code","love","you"]
# strs = ["#", "##"]
# strs = ["VeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimesVeryLongStringWithoutAnySpacesOrSpecialCharactersRepeatedManyTimes"]
# s = sol.encode(strs)
# print(s)
# print(sol.decode(s))

