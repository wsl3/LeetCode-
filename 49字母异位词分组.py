# class Solution:
#     def groupAnagrams(self, strs):
#         helper = {}
#         for str in strs:
#             print(self.convert(str))
#             temp = self.convert(str)
#             if temp in helper:
#                 helper[temp].append(str)
#             else:
#                 helper[temp] = [str]
#         return [value for value in helper.values()]
#     def convert(self, str):
#         str = list(str)
#         str.sort()
#         return "".join(str)

#     二进制相*
class Solution:
    def groupAnagrams(self, strs):
        helper = {}
        msg = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37,
               'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83,
               'x': 89,
               'y': 97, 'z': 101}
        for str in strs:
            sum = 1
            for c in str:
                sum *= msg[c]
            if sum in helper:
                helper[sum].append(str)
            else:
                helper[sum] = [str]
        return [value for value in helper.values()]


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["abc", "bcad", "sss"]))
