# 分而治之:递归式问题解决方法
from random import randint 

def quickSort(list):
	if len(list) <= 1:
		return list
	else:
		# 基准值
		basic = list[0]
		greater = [i for i in list[1:] if i>basic]
		less = [i for i in list[1:] if i<=basic]
		return quickSort(less) + [basic] + quickSort(greater)

list_test = [randint(-40, +40) for _ in range(10)]

if __name__ == "__main__":
	print(list_test)
	print(quickSort(list_test))