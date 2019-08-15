# 二分查找
# 前提:序列必须是有序的
from random import randint

def decerator(func):
	def wrapper(list, elem):
		print("list:",list)
		print("elem:",elem)
		i = func(list, elem)
		print("查找结果:i=",i)
	return wrapper

@decerator
def binary_search(list, elem):
	low, high = 0, len(list)-1
	# 这里必须使用 <= low=high时只包含一个元素
	while(low<=high):
		# 使用 // 的除法得到整数
		middle = (low+high)//2
		if list[middle] == elem:
			return middle
		if list[middle] > elem:
			high = middle-1
		else:
			low = middle+1

	return None

test_list = [randint(i,i+2) for i in range(0,16,4)]
test_list2 = [1,2,3,4,5,6,7,8,9,10]
elem = 5
elem2 = 1

if __name__ == '__main__':
	binary_search(test_list, elem)
	binary_search(test_list2, elem2)
