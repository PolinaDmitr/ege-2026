file = open('26_28801.txt')
n, k = map(int, file.readline().split())
robots = []
for i in range(n):
    arrival, charge_time, priority, battery_time = map(int, file.readline().split())
    robots.append((arrival, priority, battery_time, charge_time))

robots.sort()

stations = [()] * k
# формат arrival 0, priority 1, battery_time 2, charge_time 3, end_charge 4
# (когда закончится заряд = время, когда встал + заряд)
queue_k = []

serviced_robot = 0
discharged_robots = 0
last_station = -1

last_time = robots[-1][0]
current_robot = -1

for time in range(0, last_time * 10):
    # чистим очереди, если время = время конца, то дроп
    for j in range(k):
        if len(stations[j]) == 5 and stations[j][4] <= time:
            stations[j] = ()
    # чекаем очередь (очищаем от разрядившихся роботов)
    if len(queue_k) != 0:
        queue_k = [x for x in queue_k if x[4] >= time]
        queue_k.sort(key=lambda x: [-x[1], x[4], x[3], x[0]])
    # распределяем роботов по станциям
    if any(len(stations[j]) == 0 for j in range(k)) and len(queue_k) != 0:
        for j in range(k):
            if len(stations[j]) == 0 and len(queue_k) != 0:
                stations[j] = (queue_k[0][0], queue_k[0][1], queue_k[0][2], queue_k[0][3], time + queue_k[0][3])
                queue_k.pop(0)
                last_station = j
                serviced_robot += 1

    # ищем в списке роботов, которые прилетят в это время
    for j in range(current_robot + 1, len(robots)):
        if robots[j][0] == time:
            # если есть свободная станция, то ставим туда
            if any(len(stations[j]) == 0 for j in range(k)):
                for i in range(k):
                    if len(stations[i]) == 0:
                        stations[i] = (robots[j][0], robots[j][1], robots[j][2], robots[j][3], time + robots[j][3])
                        last_station = i
                        serviced_robot += 1
                        break
            else:
                queue_k.append((robots[j][0], robots[j][1], robots[j][2], robots[j][3], time + robots[j][2]))
            current_robot = j
        elif robots[j][0] > time:
            break

print(serviced_robot, last_station + 1)









