def merge_strings(word1, word2): #Create a function
    result = ''             #created an empty variable to store the result
    for i, j in zip(word1, word2):  #Used zip function to iterate to iterants
        result += i+j               #Stored characters in the result
    return result + word1[len(word2):] + word2[len(word1):]     #returned result plus leftovers


#Method 2

    c
print(merge_strings(word1 = "abc", word2 = "pqr"))
print(merge_strings(word1 = "ab", word2 = "pqrs"))
        
