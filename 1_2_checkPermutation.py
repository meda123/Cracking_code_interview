"""
Task: Given two strings, write a method to decide if one is a permutation of 
the other.


Hint: Two strings that are permutations should have the same characters but in 
different orders. Can you make the orders the same? 
"""

##################### First way to do it: most efficient #######################

from collections import Counter 

def same_permutation(word1, word2):

    #Fail fast check, same length? 
    if len(word1) != len(word2):
        return False

    counter = Counter()
    for letter in word1:
        counter[letter] += 1
    for letter in word2:
        if counter[letter] == 0:
            return False
        counter[letter] -= 1
    return True 
 

print same_permutation("meda", "trel")
# False 
print same_permutation("dog", "god")
#True 


"""
Written explanation 

1. Fail fast by making sure both words are the same length 

2. Note, the Counter method allows for quick tallying. For example:

from collections import Counter

counter = Counter()
for word in ['hello', 'hello', 'test']:
    counter[word] += 1 

>>> counter
Counter({'hello': 2, 'test': 1})

3. On the first loop (line 18), we create a dictionary that counts the occurence
of each letter 

On the second loop (20), we check if each letter inside word2 is present inside 
the original dictionary. 
    If a letter inside word2 is NOT present (aka count is at zero), return False
    
    If a letter inside word2 IS present, decrease the count by 1, in case you
    have repeating occurences of a letter 

"""


##################### Second way to do it: cleaner ############################

def permutations(str1, str2):

    # Fail fast, are they the same length 

    if len(str1) != len(str2):
        return False 

    if sorted(list(str1)) == sorted(list(str2)):
        return True

    return False  

print permutations("hello", "hehe")
# False 
print permutations("dog", "god")
#True 


"""
This solution is much easier to follow than the first solution but it is not
as efficient. 

"""













