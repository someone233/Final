x = input()
x = x.split(' ')
x1 = x[0]
x2 = x[1]
result = int(x1) * int(x2)

len1 = len(x1)
len2 = len(x2)
len3 = len(str(result))
maxLen = max(len1, len2, len3)

if len1 <= maxLen:
    print(' '*(maxLen-len1) + str(x1))
if len2 <= maxLen:
    print(' ' * (maxLen - len2) + str(x2))
print('-'*maxLen)
print(result)