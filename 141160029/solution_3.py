def get_price(t, prices):
    for i in range(1, len(prices)):
        if prices[i - 1][0] <= t <= prices[i][0]:
            return prices[i - 1][1]
    
def solution():
    m = int(input())
    trans = []
    for i in range(0, m):
        trans.append([int(x) for x in input().split(' ')])

    m = int(input())
    price = []
    buy = 0
    sell = 0
    for i in range(0, m):
        price.append([int(x) for x in input().split(' ')])

    for t in trans:

        p = get_price(t[0], price)
        total = p * t[1] * 100
        fee = 5 if total * 0.0002 <= 5 else total * 0.0002
        trans_fee = t[1] / 10
        com_fee = 1
        yh_fee = 0
        if t[2] == 1:
            buy += total + fee + trans_fee + com_fee + yh_fee
        else:
            yh_fee = total * 0.0001
            sell += total + fee + trans_fee + com_fee + yh_fee

    print(round(sell - buy, 2))

solution()
