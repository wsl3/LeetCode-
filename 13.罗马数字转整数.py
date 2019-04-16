class Solution(object):
    def romanToInt(self, str):
        num = 0
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        d2 = {
            "I": ("V", "X"),
            "X": ("L", "C"),
            "C": ("D", "M")
        }
        index = len(str) - 1
        i = 0
        # i 对应 str 中当前字符的下标
        while (i < index):
            # 当前字符在d2中 并且 下一个字符在 对应的集合中, 即属于特殊情况
            if ((str[i] in d2) and (str[i + 1] in d2[str[i]])):
                num += (d[str[i + 1]] - d[str[i]])
                i += 2
            # 一般情况
            else:
                num += d[str[i]]
                i += 1
        # 循环结束可能因为 i+2, i+1 , 第二种情况需要加上字后一个罗马数字对应的数值
        if (i == index):
            num += d[str[-1]]
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("IV"))
