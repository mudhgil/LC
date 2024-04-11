def kvowel(s, k):
    l = r = 0
    count = 0
    for r in range(len(s)):
        if s[r] in 'aeiou':
            count += 1
        if k<0 and s[l] == 0:
            k += 1
        l += 1
    return r-l + 1