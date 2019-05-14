# beat 90.65%
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1 or s[0] == "0":
            return 0 if s[0] == "0" else 1
        res = []
        res.append(1)
        res.append(1)

        for i in range(1, len(s)):
            temp1 = int(s[i-1:i+1])
            # int(s[i])不为0, 10=<int(s[i-1:i+1])<=26时, res[i] = res[i-1] + res[i-2]
            temp = (0 if int(s[i])==0 else res[-1]) + (0 if temp1 > 26 or temp1<10 else res[-2])

            res.append(temp)
        print(res)
        return res[len(s)]

if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("100"))
