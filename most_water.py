def water(h):
    l = 0
    r = len(h)-1
    result = 0
    currVal = 0
    while l<r:
        currVal = min(h[r], h[l])*(r-l)
        result += currVal
        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
    return result