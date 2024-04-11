def ufreq(arr):
    d = {}
    for i in arr:
        if i in d:
            count += 1
        else:
            count = 1
    return len(d.values()) == len(set(d.values()))
print(ufreq([1,1,2,3,2,3,4]))