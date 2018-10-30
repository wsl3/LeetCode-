# -*- coding:utf8 -*-
from random import randint

# 位置是否可达
def passable(list_temp, pos):
	# 首先位置不能越界
	if pos[0]>3 or pos[0]<0 or pos[1]>3 or pos[1]<0:
		return False
	return list_temp[pos[0]][pos[1]] == 0

# 对可以到达的位置做标记
def markup(list_temp, pos):
	list_temp[pos[0]][pos[1]] = 2

def search_target(start, end, list_test):
	stack = []
	# 东， 南， 西， 北
	direction = [(0,1),(1,0),(0,-1),(-1,0)]

	if start == end:
		print("success!\nstart和end相等！")
		return 
	# 先把开始位置做标记，后入栈
	markup(list_test, start)
	stack.append(start)

	# 栈非空
	while stack:
		# 获取当前所在位置
		current_pos = stack[-1]
		for i in range(4):
			# 下一个位置
			next_step = (current_pos[0] + direction[i][0],current_pos[1]+direction[i][1])

			# if next_step[0]>3 or next_step[1]>3 \
			# or next_step[0]<0 or next_step[1]<0:
			# 	continue

			if next_step == end:
				print("success!")
				stack.append(end)
				markup(list_test, next_step)
				n = 10
				print("迷宫!\nstart:{},end:{}".format(start, end))
				for li in list_test:
					print(li)
				for p in stack:
					list_test[p[0]][p[1]] = n
					n += 1
				print("start->end最终路径图，从10开始走。。。")
				for li in list_test:
					print(li)
				return 


			if passable(list_test, next_step):
				markup(list_test, next_step)
				stack.append(next_step)
				break
			elif i == 3:
				stack.pop()

	print("找不到路径！")
	return 

if __name__ == "__main__":
	# 具体例子
	# list_test = [
	# 	[0,0,1,0],
	# 	[1,0,0,0],
	# 	[1,1,0,1],
	# 	[1,1,0,0]
	# ]
	# start, end = (0,0), (3,3)
	# search_target(start, end, list_test)
		

	# 随机例子
	list_random = [ [randint(0,1),randint(0,1),randint(0,1),\
					randint(0,1)] for i in range(4)]
	start = (randint(0,3), randint(0,3))
	end = (randint(0,3), randint(0,3))

	print("随机迷宫!\nstart:{},end:{}".format(start, end))
	for i in list_random:
		print(i)

	search_target(start, end, list_random)
		






