str1=input()
list1=str1.split()
a=int(list1[0])
b=int(list1[1])
a1=a
b1=b
flag1=0
flag2=0
while a1>1:
    a1=a1/10
    flag1+=1
while b1>1:
    b1=b1/10
    flag2+=1
if flag1>=flag2:
    print(a)
    for i in range(flag1-flag2):
        print(' ',end='')
    print(b)
    for i in range(flag1):
        print('-',end='')
    print('')
    print(a*b)
else :
    for i in range(flag2-flag1):
        print(' ',end='')
    print(a)
    print(b)
    for i in range(flag2):
        print('-',end='')
    print('')
    print(a*b)
