def maxSub(nums, k):
    currSum = maxSum = sum(nums[:k])
    for i in range(k, len(nums)-1):
        currSum += nums[i] - nums[i-k]
        maxSum  = max(currSum, maxSum)
    return maxSum/k
print(maxSub(nums = [1,12,-5,-6,50,3], k = 4))