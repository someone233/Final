def solution():
    level = {
        ')': 0,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
        }

    stack = list()
    exp = reversed(input().split(' '))
    ans = list()
    for e in exp:
        if e == ')':
            stack.append(e)
            continue
        elif e == '(':
            while(stack and stack[-1] != ')'):
                  ans.append(stack[-1])
                  stack.pop()
            if stack:
                  stack.pop()
            continue
        elif e in level.keys():
            if stack and level[stack[-1]] <= level[e]:
                  stack.append(e)
            elif not stack:
                stack.append(e)
            else:
                  while (stack and level[stack[-1]] > level[e]):
                      ans.append(stack[-1])
                      stack.pop()
                  stack.append(e)
        else:
            ans.append(e)

    while(stack):
        ans.append(stack[-1])
        stack.pop()
    print(' '.join(reversed(ans)))

solution()
