# 最近距离
import math
from random import randint


class Solution(object):
    # 暴力法
    def closeSet2(self, pointSet):
        min_d = self.distance(pointSet[0], pointSet[1])
        if len(pointSet) == 2:
            return min_d
        for i in range(len(pointSet)):
            for j in range(i + 1, len(pointSet)):
                d = self.distance(pointSet[i], pointSet[j])
                min_d = min(min_d,d)
        return min_d

    # 分治法
    def closeSet(self, pointSet):
        if len(pointSet) == 2:
            return self.distance(pointSet[0], pointSet[1])

        if len(pointSet) == 3:
            d1 = self.distance(pointSet[0], pointSet[1])
            d2 = self.distance(pointSet[0], pointSet[2])
            d3 = self.distance(pointSet[1], pointSet[2])
            return d3 if d3 < (d1 if d1 < d2 else d2) else (d1 if d1 < d2 else d2)

        mid = len(pointSet) // 2
        minLeft = self.closeSet(pointSet[:mid])
        minRight = self.closeSet(pointSet[mid:])
        d = min(minLeft, minRight)  # 最小值

        p = [i for i in pointSet[:mid] if i[0] >= pointSet[mid][0] - d] + [i for i in pointSet[mid:] if
                                                                           i[0] <= pointSet[mid][0] + d]

        p = sorted(p, key=lambda x: x[1])

        for i in range(len(p)):
            for j in range(i + 1, len(p)):

                if p[j][1] - p[i][1] >= d:
                    break
                else:
                    temp_d = self.distance(p[i], p[j])
                    d = temp_d
        return d

    def distance(self, x, y):

        return math.sqrt(((x[0] - y[0]) ** 2) + ((x[1] - y[1]) ** 2))


if __name__ == "__main__":
    pointSet = []
    for i in range(10):
        temp = (randint(0, 10), randint(0, 10))
        pointSet.append(temp)

    s = Solution()
    pointSet = sorted(pointSet, key=lambda x: x[0], reverse=False)
    print(pointSet)
    print("暴力法: ", s.closeSet(pointSet))
    print("分治法: ", s.closeSet2(pointSet))
