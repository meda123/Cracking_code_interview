
"""
Given a string, write a function to check if it's a permutation of a palidrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words.

>>> pal_permutation("Tact Coa")
True 

(permutations: "taco cat", "atco cta", etc)

"""

from collections import Counter 

example = "Tact Coa"
exa2 = "taco cat"

def pal_permutation(words, permutation):

    words = words.replace(' ', '').lower()

    return sum(freq%2 for freq in Counter(words).values()) < 2 


test = pal_permutation(example,exa2)
print test 


