class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['{', '[', '(']
        temp = {
        	'}':'{',
        	']':'[',
        	')':'('
        }
        for i in s:
        	if i in left:
        		# 左括号入栈
        		stack.append(i)
        	else:
        		# 右括号和栈顶括号进行比较
        		right_ = temp.get(i)
        		# 栈非空时取出栈顶括号
        		if stack:
        			left_ = stack.pop()
        		else:
        			# 存在右括号，没有左括号则return False
        			return False
        		# 左右括号不匹配
        		if right_ != left_:
        			return False
        if stack:
        	# 栈非空时返回False
        	return False
        return True

        