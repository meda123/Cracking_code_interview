"""
Task: Given two strings, write a method to decide if one is a permutation of 
the other.


Hint: Two strings that are permutations should have the same characters but in 
different orders. Can you make the orders the same? 
"""
from collections import Counter 

def same_permutation(word1, word2):

    #Fail fast check, same length? 
    if len(word1) != len(word2):
        return False

    counter = Counter()
    for word in word1:
        counter[word] += 1
    for word in word2:
        if counter[word] == 0:
            return False
        counter[word] -= 1
    return True 
 

print same_permutation("meda", "trel") 


