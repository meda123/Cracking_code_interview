"""
1.1 isUnique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures

"""

# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


################################## Explanation ################################ 
"""
 
What is char_set = [False for _ in range(128)] doing? 
    It is creating a list of 128 False items. The _ is a throwaway function value.
    It is a list comprehension, a pretty neat Python tool. Below is a basic list
    comprehension examples. 

    char_set = ["Medalis" for _ in range(5)]
    >>> ['Medalis', 'Medalis', 'Medalis', 'Medalis', 'Medalis']

    
    words = "I love writing code in python".split()
    adjust_words = [[word.upper(), word.lower()] for word in words]

    for adjust_word in adjust_words:
        print adjust_word

    >>> ['I', 'i']
    >>> ['LOVE', 'love']
    >>> ['WRITING', 'writing']
    >>> ['CODE', 'code']
    >>> ['IN', 'in']
    >>> ['PYTHON', 'python']



In human words, what is this algorithm doing? 

 SUMMARY:
    Create an array of boolean values, where the glad at index i indicates whether
    character i in the alphabet is contained in the string. The second time you 
    see this character, you can immediately return False. 


    STEP-BY-STEP: 

    The first question we should ask the interviewer, is if the string is an 
    ASCII string or a Unicode string. In this case, we'll assume that this 
    character set is ASCII. Note we are check agains 128-character alphabet, but
    it is also okay to assume 256 characters (extended ASCII).

    If lines 12 & 13, we check that our string is NOT longer than 128 characters
    because if it is longer, than it is definitely not composed of unique characters. 

    In line 16, we create our char_set list that has 128 items, all with the value
    False. 

    In line 18, we loop through each characters in the string. We save the value
    of each character (line 19) using the ord buit-in function which returns a
    corresponding ASCII value given a single character. 

    If a character (say the ASCII value of "a" is 10) is True, meaning at 
    index 10 our char_set list's value is NOT False, but instead True --> we 
    return False. We return False because that means "a" has been found in the 
    list already. This is all line 20. 

    Wait what? It makes a little more sense after looking at line 23. If our 
    if statement in line 20 is NOT met, we jump to line 23, where char_set[val]
    is set to True. Looking at an example (say the ASCII value of "e" is 15), in 
    line 23 we are saying:

                char_set[15] = True
    Therefore, next time when we do run into the value "e", we'll return False
    because we already found "e" before.

    Lastly, in line 25, once we have looped through all characters in the string
    and we have NOT found repeating characters, we return True (as in, a string
    is indeed unique).  

"""




##################################### TEST ##################################    

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()