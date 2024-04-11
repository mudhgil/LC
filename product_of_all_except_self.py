def product(arr):
    l = len(arr)
    pre = 1
    post = 1
    result = [1]*l
    for i in range(l):
        result[i] *= pre
        pre = pre * arr[i]
        result[l-1-i] *= post
        post = post * arr[l-1-i]
    return result
print(product(arr=[1,2,3,4]))

#Very unique and fresh question, the idea is to use commulative multiplication 
# in the current iter, keep updating result and iter in every iteration.