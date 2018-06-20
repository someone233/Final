# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:42:46 2018

@author: lenovo
"""

s1=input("please input:")
s2=input("input the location:")
n=int(s1.split()[0])
p=int(s1.split()[1])
s3=s2.split()
location=[]
answer=0
for i in range(0,len(s3)):
    location.append(int(s3[i]))
if(p>=n):
    print(0)
else:
    distance=[]
    for i in range(0,n):
        a=[]
        for j in range(0,n):
            a.append(abs(location[j]-location[i]))
        distance.append(a)
    locate=[]
    for i in range(1,p+1):
        t=((location[n-1]+location[0])//(p+1))*i
        minx=location[n-1]-location[0]
        miny=0
        for j in range(0,n):
            if(abs(location[j]-t)<minx):
                minx=abs(location[j]-t)
                miny=j
        locate.append(miny)
    for i in range(0,n):
        answer+=min([distance[i][j] for j in locate])
    print(answer)