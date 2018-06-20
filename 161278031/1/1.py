# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 09:55:52 2018

@author: wangjing
"""

x=input("please input:")
y=x.split()
out=str(int(y[0])*int(y[1]))
m=len(out)
if(int(y[0])<int(y[1])):
    s=y[0]
    y[0]=y[1]
    y[1]=s
y[0]=' '*(m-len(y[0]))+y[0]
y[1]=' '*(m-len(y[1]))+y[1]
print(y[0]+"\n"+y[1]+"\n"+"-"*m+"\n"+out)