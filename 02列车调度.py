def solution(car, car2):
	stack = []
	result = []
	a = 0
	for i in car:
		# 只要栈中有匹配的元素就全部移动到2轨道
		while stack and stack[-1] == car2[a]:
			stack.pop()
			a += 1
			result.append("3->2")
		if i == car2[a]:
			result.append("1->2")
			a += 1
		else:
			result.append("1->3")
			stack.append(i)
	# 如果此时栈空代表列车移动结束
	if not stack:
		for i in result:
			print(i)
		return 
	# 栈不为空，把栈中的元素移动到2轨道
	while stack:
		if stack[-1] == car2[a]:
			result.append("3->2")
			a += 1
			stack.pop()
		else:
			break
	# 全部移到2轨道
	if a == len(car) and not stack:
		for i in result:
			print(i)
	# 不能移动到2轨道
	else:
		print("Are you kidding me?")
	return 


car = input()
car2 = input()
solution(car, car2)
		
		
		

