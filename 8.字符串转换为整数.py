class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = ""
        str = str.strip()

        if str == "" or (ord(str[0]) >= ord("a") and ord(str[0]) <= ord("z")) or ( \
                        ord(str[0]) >= ord("A") and ord(str[0]) <= ord("Z")):
            return 0

        for i in enumerate(str):
            if ord(i[1])>=48 and ord(i[1])<=57:
                result += i[1]
            elif (i[1]=="+" or i[1]=="-") and i[0] == 0:
                continue
            else:
                break
        if result == "":
            return 0
        if str[0] == "-":
            num = int(result) if int(result) <= 2**31 else 2**31
            return -num
        else:
            num = int(result) if int(result) <= 2**31-1 else 2**31-1
            return num

if __name__ == "__main__":
    print(Solution().myAtoi("    32"))