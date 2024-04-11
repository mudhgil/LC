# def alternatively(word1, word2):
# 	result = ''
# 	for i, j in zip(word1, word2):
# 		result += i+j
# 	return result + word1[len(word2):] + word2[len(word1):]
# print(alternatively(word1 = "abcd", word2 = "pq"))

# def alternatively(word1, word2):
#     result = ''
#     for i in range(min(len(word1), len(word2))):
#         result += word1[i] + word2[i]
#     return result + word1[i+1:] + word2[i+1:]
# print(alternatively(word1 = "abcd", word2 = "pq"))
# import math
# def g(s, t):
#     if s + t != t + s:
#         return ''
#     return s[:math.gcd(len(s), len(t))]
# print(g(s = "ABABAB", t = "ABAB"))

# def candy(candies, extraCandies):
#     return [candy + extraCandies >= max(candies) for candy in candies]
# print(candy(candies = [2,3,5,1,3], extraCandies = 3))
# print(candy(candies = [4,2,1,1,2], extraCandies = 1))

# import math
# def common(str1, str2):
#     return str1[:math.gcd(len(str1), len(str2))]
# print(common(str1 = "ABCABC", str2 = "ABC"))

# candies = [3,2,5,4,9]
# def candy(candies, extraCandies):
#     return [candy + extraCandies >= max(candies) for candy in candies]

# def flower(flowerbed, n):
#     if n == 0:
#         return True
#     for i in range(len(flowerbed)):
#         if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
#             flowerbed[i] == 1
#             n -= 1
#             if n == 0:
#                 return True
#     return False
# print(flower(flowerbed = [1,0,0,0,0,0,1], n = 2))


#Reverse vowel

# def reverseVowel(str1):
#     s = list(str1)
#     result = ''
#     vowel = 'aeiouAEIOU'
#     l = 0
#     r = len(str1)-1
#     while l<r:
#         if s[l] in vowel and s[r] in vowel:
#             s[l], s[r] = s[r], s[l]
#             l += 1
#             r -= 1
#         elif s[l] not in vowel:
#             l += 1
#         else:
#             s[r] not in vowel
#             r -= 1
#     return ''.join(s)
# print(reverseVowel('hello'))

#reverse string

# def reverse(s):
#     # result = ''
#     x = s.split(' ')[::-1]
#     return ' '.join(x) 
# print(reverse('the sky is blue'))

#Product of array except self
# def productArray(arr):
#     l = len(arr)
#     pre = 1
#     post = 1
#     result = [1]*l
#     for i in range(l):
#         result[i] *= pre
#         pre = pre*arr[i]
#         result[l-1-i] *= post
#         post = post*arr[l-1-i]
#     return result
# print(productArray([49.0999999,3.09,4,2,6]))





def productSelf(arr):
    pre = 1
    post = 1
    l = len(arr)
    result = [1]*l
    for i in range(l):
        result[i] *= pre
        pre = arr[i]*result[i]
        result[l-1-i] *= post
        post = arr[i]*result[l-1-i]
    return result
print(productSelf([49.0999999,3.09,4,2,6]))














