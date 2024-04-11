def reverse_string(s):
    s = s.split()[::-1]
    return  ' '.join(s)
print(reverse_string('This is my car'))