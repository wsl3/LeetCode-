class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
        	return 0
        s = str(x)
        print(s)
        if s[-1] == "0":
        	s = s[0:-1]
        if x<0:
        	s = s[1:]
        	result = -int(s[::-1])
        else:
        	result = int(s[::-1])
        if result<-2**31 or result> 2**31-1:
        	return 0
        return result

if __name__ == "__main__":
	print(Solution().reverse(-1230))