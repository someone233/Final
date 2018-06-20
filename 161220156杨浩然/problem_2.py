peopleNUm = int(input())
timeSeries = input()
timeSeries = timeSeries.split(' ')

win1 = []
win2 = []
win3 = []

for each in timeSeries:
    if len(win1) == len(win2) == len(win3):
        win1.append(timeSeries.index(each))
    elif min(len(win1), len(win2), len(win3)) == len(win1):
        win1.append(timeSeries.index(each))
    elif min(len(win1), len(win2), len(win3)) == len(win2):
        win2.append(timeSeries.index(each))
    elif min(len(win1), len(win2), len(win3)) == len(win3):
        win3.append(timeSeries.index(each))

time1 = 0
for j in range(1, len(win1)):
    time = 0
    for i in range(0, j):
        time = time + int(timeSeries[win1[i]])
    time1 = time1 + time
win1Last = time1 + int(timeSeries[win1[len(win1)-1]])

time2 = 0
for j in range(1, len(win2)):
    time = 0
    for i in range(0, j):
        time = time + int(timeSeries[win1[i]])
    time2 = time2 + time
win2Last = time2 + int(timeSeries[win2[len(win2)-1]])

time3 = 0
for j in range(1, len(win3)):
    time = 0
    for i in range(0, j):
        time = time + int(timeSeries[win1[i]])
    time3 = time3 + time
win3Last = time3 + int(timeSeries[win3[len(win3)-1]])

sumTime = time1 + time2 + time3
print('按老排队方式，顾客的总等待时间为：' + str(sumTime))
print('按老排队方式，最后一位顾客完成的时间为：' + str(max(win1Last, win2Last, win3Last)))

time = 0
win1 = []
win2 = []
win3 = []

for each in timeSeries:
    if len(win1) != 0 and time == int(win1[0]):
        win1 = []
    if len(win2) != 0 and time == int(win2[0]):
        win2 = []
    if len(win3) != 0 and time == int(win3[0]):
        win3 = []
    if len(win1) == 0:
        win1.append(timeSeries.index(each))
    elif len(win2) == 0:
        win2.append(timeSeries.index(each))
    elif len(win3) == 0:
        win3.append(timeSeries.index(each))
    else:
        time += 1