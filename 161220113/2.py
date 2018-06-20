n=int(input("please input N:"))
strlist=input().split()
list1=[]
list2=[]
list3=[]
for i in strlist:
    i=int(i)
    temp=min(len(list1),len(list2),len(list3))
    if (temp==len(list1)):
        list1.append(i)
    elif (temp==len(list2)):
        list2.append(i)
    elif (temp==len(list3)):
        list3.append(i)
lenlist1=len(list1)-1
lenlist2=len(list2)-1
lenlist3=len(list3)-1
time1=0
time2=0
time3=0
for i in list1:
    time1+=i*lenlist1
    lenlist1=lenlist1-1
for i in list2:
    time2+=i*lenlist2
    lenlist2=lenlist2-1
for i in list3:
    time3+=i*lenlist3
    lenlist3=lenlist3-1
print("W1=",time1+time2+time3,"T1=",max(sum(list1),sum(list2),sum(list3)))
for i in strlist:
    i=int(i)
lis1=int(strlist[0])
lis2=int(strlist[1])
lis3=int(strlist[2])
i=3
time=0
while (i<=n-1):
    time=time+min(lis1,lis2,lis3)
    lis1=lis1-min(lis1,lis2,lis3)
    lis2=lis2-min(lis1,lis2,lis3)
    lis3=lis3-min(lis1,lis2,lis3)
    if(lis1==0):
        lis1=int(strlist[i])
        i=i+1
    if(lis2==0):
        lis2=int(strlist[i])
        i=i+1
    if(lis3==0):
        lis3=int(strlist[i])
        i=i+1
print("W2=",time,"T2=",time-int(strlist[n-1]))
        
    
    
    
    
        
    

