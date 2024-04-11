def maxones(nums):
    n = len(nums)
    l = r = 0
    ans = 0
    zeroes = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeroes += 1
        while zeroes > 1:
            if nums[l] == 0:
                zeroes -= 1
            l += 1
        ans = max(ans, r-l+1-zeroes)
    return ans-1 if ans == n else ans
print(maxones([0,1,1,1,0,1,1,0,1]))
        