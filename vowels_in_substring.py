def maxVowel(s, k):
    # result = 0
    count = 0
    vowel = 'aeiou'
    for i in range(len(s)):
        if s[i] in vowel:
            count += 1
        if i >= k:
            if s[i-k] in vowel:
                count -= 1
        # result = max(result, count)
    return count
print(maxVowel(s = "abciiidef", k = 3))
