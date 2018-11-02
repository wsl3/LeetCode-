class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        back_sub = ''
        back_sub_len = 0
        max_back_sub = ''
        max_back_sub_len = 0
        for char in s:
            if char in back_sub:
                # 　如果char在back_sub中的话要查看每一种情况.back_sub中可能有多个char
                for i in [i for i in range(back_sub_len) if char == back_sub[i]]:

                    temp = back_sub[i:] + char

                    temp_len = back_sub_len - i + 1
                    #　temp 是回文串
                    if temp == temp[::-1]:
                        if temp_len >= max_back_sub_len:
                            max_back_sub_len = temp_len
                            max_back_sub = temp

            back_sub += char
            back_sub_len += 1
        # 如果没有回文串就返回字符串的第一个字符
        return max_back_sub if max_back_sub_len else s[0]


if __name__ == "__main__":
    print(Solution().longestPalindrome("babadada"))
