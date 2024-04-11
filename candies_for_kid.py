def candy_kid(candies, extraCandies):
    return [candy+extraCandies >= max(candies) for candy in candies]
print(candy_kid(candies = [2,3,5,1,3], extraCandies = 3))