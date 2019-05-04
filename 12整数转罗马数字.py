
# beat 75%
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        num = str(num)
        nums = [int(n) * pow(10, (len(num) - i - 1)) for i, n in enumerate(num)]
        for i in nums:
            roman = roman + self.getString(i)
        return roman

    def getString(self, i):
        d = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",

            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM"
        }
        if d.get(i, None):
            return d.get(i)
        length = len(str(i))
        if(length == 4):
            return "M"*int(str(i)[0])
        elif (length==3):
            return "C"*int(str(i)[0]) if i<500 else ("D"+("C"*(int(str(i)[0])-5)))
        elif (length==2):
            return "X"*int(str(i)[0]) if i<50 else ("L"+("X"*(int(str(i)[0])-5)))
        else:
            return "I"*int(str(i)[0]) if i<5 else ("V"+("I"*(int(str(i)[0])-5)))

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3999))
