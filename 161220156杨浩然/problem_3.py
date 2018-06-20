transactionNum = int(input())
transactionRecord = []
for i in range(0, transactionNum):
    x = input()
    transactionRecord.append(x.split(' '))

priceChangeNum = int(input())
priceChangeRecord = []
for j in range(0, priceChangeNum):
    x = input()
    priceChangeRecord.append(x.split(' '))

expense = 0
receive = 0

for each in transactionRecord:
    t = int(each[0])
    a = int(each[1])
    d = int(each[2])
    p = 0
    for i in range(0, priceChangeNum):
        if i < priceChangeNum-1 and t >= int(priceChangeRecord[i][0]) and t < int(priceChangeRecord[i+1][0]):
            p = int(priceChangeRecord[i][1])
        elif i == priceChangeNum-1 and t>= int(priceChangeRecord[i][0]):
            p = int(priceChangeRecord[i][1])
    if d == 1:
        expense = a*100*p
        fee1 = expense * 0.002
        if fee1 < 5:
            fee1 = 5
        expense = expense + fee1
        fee2 = int(a*100/1000)
        expense = expense + fee2 + 1
    if d == 2:
        receive = a*100*p
        fee1 = expense * 0.002
        if fee1 < 5:
            fee1 = 5
        receive = receive - fee1
        fee2 = int(a * 100 / 1000)
        receive = receive - fee2 - 1

revenue = receive - expense
print('%.2f' % revenue)