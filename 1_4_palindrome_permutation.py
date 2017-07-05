
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

Note - A permutation is a string that is the same forwards and backwards.

What does it mean to be able to write a set of characters the same way forward
and backwards? We need an even of almost all characters, so that half can be on
one side and half can be on the other side. At most one character (middle one)
can have an odd count. 

To be more precise, strings with even lengths must have all even counts of chars
Strings of odd length, must have exactly 1 char with an odd count 

One-liner explanation (line #28): 
    
    Assume words = "Mama paPa"

    Counter(words) = Creates a dictionary to count frequency of each letter
    >>> Counter({'a': 4, 'p': 2, 'm': 2})

    Counter(words).values = Creates of list of all values in the dict 
    >>> [4, 2, 2]

    List comprehension to check for even number of each letter (4 % 2 = 0), 
    (2 % 2 = 0), and (2 % 2 = 0)

    fre%2 for freq in Counter(words).values()
    >>> [0, 0, 0]

    Lastly, the add all those values 0 + 0 + 0 = 0








"""



##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
