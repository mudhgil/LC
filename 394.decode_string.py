def decode(s):
    stack = []
    currNum = 0
    currString = ''
    
    for c in s:
        if c == '[':
            stack.append(currString)
            stack.append(currNum)
            currString = ''
            currNum = 0
            
        elif c == ']':
            prevNum = stack.pop()
            prevString = stack.pop()
            currString = prevString + prevNum*currString
        elif c.isdigit():
            currNum = currNum*10 + int(c)
        else:
            currString += c
    return currString
print(decode('3[ab]2[a]'))
