def solution(people_num, window_num, queue):
    # 等待时间列表,便于求最大等待时间
    wait_time = []
    # 各个窗口的服务人数
    window_server_num = [0] * window_num
    # 各个窗口
    windows = [0] * window_num

    while queue:
        person = queue.pop(0)
        flag = 0
        # 最大服务时间为60分钟
        person[1] = person[1] if person[1] <= 60 else 60

        # 先查看是否有空窗口
        for i in range(window_num):
            # 有空窗口
            if person[0] >= windows[i]:
                windows[i] = person[0] + person[1]
                window_server_num[i] += 1
                flag = 1
                break

        if flag == 1:
            continue
        # 没有找到空窗口
        # 找到最先离开的窗口
        time_first_leave = min(windows)
        for i in range(window_num):
            if time_first_leave == windows[i]:
                break
        # 更新等待时间,人的离开时间,窗口的服务人数
        wait_time.append(windows[i] - person[0])
        windows[i] += person[1]
        window_server_num[i] += 1

    if wait_time:
        avge_wait_time = sum(wait_time) / people_num
        wait_time_max = max(wait_time)
    else:
        avge_wait_time = 0
        wait_time_max = 0


    last_leave = max(windows)
    print("%.1f %d %d" % (avge_wait_time, wait_time_max, last_leave))

    print("%d" % window_server_num[0], end="")
    for i in range(1, window_num):
        print(" %d" % window_server_num[i], end="")
    return 0


if __name__ == "__main__":
    people_num = int(input())
    queue = []
    for i in range(people_num):
        person = input().split()
        temp = [int(person[0]), int(person[1])]
        queue.append(temp)
    window_num = int(input())
    solution(people_num, window_num, queue)
