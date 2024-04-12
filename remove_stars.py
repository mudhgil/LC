def remove(s):
    stack = []
    for i in s:
        if i == '*':
            stack.pop()
        else:
            stack += i
    return ''.join(stack)
print(remove('leet**code*'))