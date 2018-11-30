class TNode(object):
    def __init__(self, char, left=None, right=None):
        self.char = char  #char是元组类型 (字符, 权重)
        self.left = left
        self.right = right

    def __repr__(self):
        return "<TNode: {}>".format(self.char)


def solution(char, weight, weight_array):
    sum = hufCode(char, weight)
    for i in weight_array:
        if i == sum:
            print("Yes")
        else:
            print("No")


def hufCode(char, weight):
    sum = 0

    # 记录各个字符的编码长度
    code_weight = {c: 0 for c in char}
    # 二叉树结点列表
    tree = [TNode((c, w)) for c, w in zip(char, weight)]
    while len(tree) != 1:
        # 获得最小的两个结点
        tree.sort(key=lambda node: node.char[1], reverse=True)
        node1 = tree.pop()
        node2 = tree.pop()

        new_node = TNode((node1.char[0] + node2.char[0], node1.char[1] + node2.char[1]))
        tree.append(new_node)

        for i in new_node.char[0]:
            code_weight[i] += 1
    for c, w in zip(char, weight):
        sum += code_weight[c] * w
    return sum


def isPreCode(L):
    # 用来判断是不是前缀编码
    flag = False
    temp = sorted(L, key=len)
    length = len(temp)
    for i in range(length):
        for j in range(i + 1, length):
            if (len(temp[i]) < len(temp[j])) and (temp[i] == temp[j][:len(temp[i])]):
                flag = True
                break
        if flag:
            break
    return flag


def strWeight(weight, str):
    # 计算路径长度
    sum = 0
    for w, s in zip(weight, str):
        sum += w * len(s)
    return sum


if __name__ == "__main__":
    num = int(input())
    char_and_weight = input().split()
    char = char_and_weight[::2]
    weight = char_and_weight[1::2]
    weight = [int(i) for i in weight]

    num_group = int(input())

    weight_array = []
    for i in range(1, num_group + 1):
        temp = []
        for _ in range(num):
            temp.append(input().split()[1])
        flag = isPreCode(temp)
        if not flag:  # 不是前缀编码
            weight_array.append(strWeight(weight, temp))
        else:  # 是前缀编码
            weight_array.append("1")
    solution(char, weight, weight_array)
