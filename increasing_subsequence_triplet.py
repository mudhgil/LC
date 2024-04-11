def triplet(arr):
    first = float('inf')
    second = float('inf')
    for num in arr:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False
print(triplet(arr=[5,4,3,2,1]))