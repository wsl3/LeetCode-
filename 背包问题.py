# 0/1背包问题


class Solution(object):
    """
    :param index: 第几个物品
         leftWeight: 背包剩下的容量
         weights: 物品数量的列表
         values: 价值列表
    """
    def mostValue(self, index, leftWeight, weights, values):
        if index == 0:
            return 0

        if(leftWeight < weights[index-1]):
            return self.mostValue(index-1, leftWeight, weights, values)
        # 不放入当前物品的价值
        a = self.mostValue(index-1, leftWeight, weights, values)
        # 放入当前物品后的价值
        b = self.mostValue(index-1, leftWeight-weights[index-1],weights,values) + values[index-1]
        return max(a,b)


if __name__ == "__main__":
    s = Solution()

    v = [8, 10, 6, 3, 7, 2]

    w = [4, 6, 2, 2, 5, 1]
    m = 6

    c = 12
    print(s.mostValue(m, c, w, v))
