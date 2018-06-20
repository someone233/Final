# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:07:08 2018

@author: Cheng
"""

x = input()
x = x.split(' ')
a = int(x[0])
b = int(x[1])
c = a*b
n1 = len(x[0])
n2 = len(x[1])
n3 = len(str(c))

for i in range(n3-n1):
    print(' ', end='')
print(a)
for i in range(n3-n2):
    print(' ', end='')
print(b)
for i in range(n3):
    print('-', end='')
print()
print(c)
