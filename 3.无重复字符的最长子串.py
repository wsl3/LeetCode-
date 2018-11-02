class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        result = []
        for i in range(len(s)):
            num, t= 1, 0
            temp = {}
            temp[s[i]] = num
            for j in range(i+1, len(s)):
                if s[j] in temp:
                    t = j
                    break
                t = j + 1
                num += 1
                temp[s[j]] = num
            result.append(temp[s[t-1]])
        return max(result)

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("ab"))