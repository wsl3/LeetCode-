# 广度优先搜索是基于图的一种算法
# 主要为了解决最短路径问题

from collections import deque



def is_you_find(person):
	return person=="jonny"

def search_person(net):
	d = deque()
	d = d+deque(net["you"])
	# 创建已经找过的人的列表
	have_found = []
	while(net is not None):
		person = d.popleft()
		# person不在已经查找的人中
		if person not in have_found:
			print(person, end=" ")
			# 找到了人
			if is_you_find(person):
				return person
			# 没找到，把他的朋友的列表添加到deque后面，继续找下一个
			else:
				d = d+deque(net[person])
		have_found.append(person)
	return False





net = {}
net["you"] = ["bob", "alice", "claire"]
net["bob"] = ["anju", "peggy"]
net["alice"] = ["peggy"]
net["claire"] = ["thoh", "jonny"]
net["anju"] = []
net["peggy"] = []
net["thoh"] = []
net["jonny"] = []

if __name__ == "__main__":
	print(search_person(net))

