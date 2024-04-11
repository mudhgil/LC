import math
def str_gcd(s, t):
    if s + t != t + s:
        return ''
    return t[:math.gcd(len(s), len(t))]
print(str_gcd(s = "ABCABC", t = "ABC"))