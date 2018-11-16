def solution(node_num, relationship):
    for node in range(1, node_num + 1):
        num = 1

        queue = deque([(node, 0)])
        msg = {}
        msg[node] = 1
        while queue:
            temp = queue.popleft()
            for i in relationship:
                if (temp[0] == i[0]) and (i[1] not in msg) and (temp[1] < 6):
                    queue.append((i[1], temp[1] + 1))
                    msg[i[1]] = 1
                    num += 1
                if (temp[0] == i[1]) and (i[0] not in msg) and (temp[1] < 6):
                    queue.append((i[0], temp[1] + 1))
                    msg[i[0]] = 1
                    num += 1
        print("%d: %.2f" % (node, (num / node_num)*100)+r"%")
    return 0

if __name__ == "__main__":
    from collections import deque

    temp = input().split()
    node_num = int(temp[0])
    side_num = int(temp[1])
    relationship = []
    for i in range(side_num):
        temp = input().split()
        relationship.append((int(temp[0]), int(temp[1])))
        # relationship.append((int(temp[1]), int(temp[0])))
    solution(node_num, relationship)
