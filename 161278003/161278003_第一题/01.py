a = input('请输入a:')
b = input('请输入b:')
a = int(a)
b = int(b)
a_size = 0
b_size = 0
a_ = a
b_ = b
while a_!=0:
    a_ = a_//10
    a_size += 1
while b_!=0:
    b_ = b_//10
    b_size += 1
c = a*b
if a_size > b_size:
    _size = a_size - b_size
    print(a)
    for i in range(0,_size):
        if i == _size - 1:
            print(' '+str(b))
        else:
            print(' ')
    print('--')
    print(c)
else:
    _size = b_size - a_size
    for i in range(0,_size):
        if i == _size - 1:
            print(' '+str(a))
        else:
            print(' ')
    print(b)
    print('--')
    print(c)
