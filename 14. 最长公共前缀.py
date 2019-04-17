class Solution:
    def longestCommonPrefix(self, List):
        if not List:
            return ""
        if len(List)==1:
            return List[0]
        List.sort(key=len)

        first = List[0]
        List = List[1:]

        for i, c in enumerate(first):
            for str in List:
                if(str[i] == c):
                    continue
                else:
                    return first[:i]
        return first






if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))
