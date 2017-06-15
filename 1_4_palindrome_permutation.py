
"""
Given a string, write a function to check if it's a permutation of a palidrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words.

>>> pal_permutation("Tact Coa")
True 

(permutations: "taco cat", "atco cta", etc)

"""

example = "Tact Coa"
exa2 = "taco cat"

def pal_permutation(words, permutation):

    if len(words) != len(permutation):
        return False

         









test = pal_permutation(example,exa2)
print test 


