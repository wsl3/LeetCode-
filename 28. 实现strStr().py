# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         if (needle == ""):
#             return 0
#         len1, len2 = len(haystack), len(needle)
#         for i, c in enumerate(haystack):
#             j = 0
#             if (c == needle[j]):
#                 while (j<len2 and (j+i)< len1 and haystack[i + j] == needle[j]):
#                     j += 1
#                 if(j == len2):
#                     return i
#         return -1


# Sunday算法
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (needle == ""):
            return 0
        len1, len2 = len(haystack), len(needle)
        i, j = 0, 0
        while(i<= len1-len2):
            if(haystack[i] != needle[j]):
                if(i+len2 )


if __name__ == "__mian__":
    pass
