"""
Task: Given two strings, write a method to decide if one is a permutation of 
the other.


Hint: Two strings that are permutations should have the same characters but in 
different orders. Can you make the orders the same? 
"""
word1 = "hello"
word2 = "eholl"


same = {}

def same_permutation(word1, word2):

    #Fail fast check, same length? 
    if len(word1) != len(word2):
        return False

    #Order word2 to look like word1 
    for i in range(len(word2)): 
      
        word_2_change = word2[i+1:len(word2)] + word2[i]
        print word_2_change

same_permutation(word1, word2) 


