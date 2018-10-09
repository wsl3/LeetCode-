# 链表节点类
class Node(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class Solution(object):
    def __init__(self):
        self.head = None
       
    def create_list(self, people):
        self.head = Node(0)
        p = self.head
        for i in range(1, people+1):
            temp = Node(i)
            p.next_, p = temp, temp
        p.next_ = self.head.next_

    def is_empty(self):
        return self.head.next_.next_ == self.head.next_

    def solution(self, people, p):
        # 条件判断
        if people<1 or people>3000 or\
           p<1 or p>5000:
            print("people或p输入有误！")
            return
       
        result = []
        # 创建链表
        self.create_list(people)
        pre = self.head
       
        while not self.is_empty():
           
            # 找到要删除节点的前驱
            for _ in range(p-1):
                pre = pre.next_
            temp  = pre.next_
            result.append(temp.elem)
           
            if self.head.next_ == temp:
                self.head.next_ = temp.next_
            pre.next_ = temp.next_
           
        result.append(self.head.next_.elem)
        for i in result:
            print(i, end=" ")

if __name__ == "__main__":
    solution = Solution()
    solution.solution(7, 3)