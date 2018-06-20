# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:15:36 2018

@author: lenovo
"""

def expense(price,count):
    money=price*0.002
    if(money<5):
        money=5
    money+=(count//1000)
    money+=1
    return money

m=int(input("please input the number of action:"))
action=[]
for i in range(0,m):
    s=input().split()
    action.append([int(s[0]),int(s[1]),int(s[2])])
n=int(input("input the change number:"))
change=[]
for i in range(0,n):
    s=input().split()
    change.append([int(s[0]),int(s[1])])

output=0
revenue=0
for i in range(0,len(action)):
    for j in range(0,len(change)-1):
        if(action[i][0]>=change[j][0] and action[i][0]<change[j+1][0]):
            price=change[j][1]
            break
    if(action[i][0]>=change[len(change)-1][0]):
        price=change[len(change)-1][1]
    if(action[i][2]==1):
        output+=price*action[i][1]*100
        output+=expense(price*action[i][1]*100,action[i][1]*100)
    else:
        revenue+=price*action[i][1]*100
        output+=expense(price*action[i][1]*100,action[i][1]*100)+price*action[i][1]*100*0.001
print("the allowance is: %.2f" %(revenue-output))