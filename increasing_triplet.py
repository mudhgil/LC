def triple(arr):
    first_small = float('inf')
    second_small = float('inf')
    for num in arr:
        if first_small>=num:
            first_small = num
        elif second_small >= num:
            second_small = num
        else:
            return True
    return False
print(triple([1,2,3,4, 5]))
            