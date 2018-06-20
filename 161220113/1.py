a=int(input("please input a:"))
b=int(input("please input b:"))
lena=len(str(a))
lenb=len(str(b))
if(lena>lenb):
    print(a)
    for i in range(0,lena-lenb):
        print(" ",end='')
        print(b)
        print("--")
        print(a*b)
elif(lenb>lena):
    print(b)
    for i in range(0,lenb-lena):
        print(" ",end='')
        print(a)
        print("--")
        print(a*b)
elif(lenb==lena):
    print(a)
    print(b)
    print("--")
    print(a*b)