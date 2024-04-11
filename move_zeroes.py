def zeroes(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    return arr
print(zeroes([0,0,10,2,0,5,4,3,2]))




