class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        sub_len = 0
        max_len = 0
        for char in s:
            if char in sub:
                if sub_len>max_len:
                    max_len = sub_len
                index = sub.index(char)
                sub = sub[index+1:] + char
                sub_len = len(sub)
            else:
                sub += char
                sub_len += 1
        if sub_len>max_len:
            max_len = sub_len
        return max_len
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abc"))