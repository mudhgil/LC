def destroy(asteroid):
    s = []
    for a in asteroid:
        while s and s[-1]>0 and a<0:
            if s[-1] + a < 0:
                s.pop()
            elif s[-1] + a<0:
                break
            else:
                s.pop()
                break
        else:
            s.append(a)
    return s
print(destroy([10, 5, -2]))