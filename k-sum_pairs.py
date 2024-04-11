def ksum(nums, k):
    count = 0
    l = 0
    r = len(nums)-1
    while l<r:
        if nums[l] + nums[r] == k:
            l += 1
            r -= 1
            count +=1
        elif nums[l] + nums[r] > k:
            l += 1
        else:
            r -= 1
    return count
print(ksum([3,1,3,4,3], k = 6))