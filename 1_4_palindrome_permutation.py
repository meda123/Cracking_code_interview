
"""
Given a string, write a function to check if it's a permutation of a palidrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words.

"""

from collections import Counter 


def pal_permutation(words):
    """ 
    >>> pal_permutation("Mama paPa")
    True

    >>> pal_permutation("Medalis Trelles")
    False

    >>> pal_permutation("Taco Cat")
    True

    """

    words = words.replace(' ', '').lower()

    return sum(freq%2 for freq in Counter(words).values()) < 2   


"""
Approach:



"""



##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
