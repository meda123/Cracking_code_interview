"""
Write a method to replace all spaces in a string with '%20'. 

NOTE: For those solving problem in Java, you may assume that 
the string has sufficient space at the end to hold the additional characters, and
that you are given the "true" length of the string. 

"""

def urlify(sentence, true_len):
    """
    >>> urlify("Mr John Smith   ", 13)
    'Mr%20John%20Smith'

    >>> urlify("much ado about nothing      ", 22)
    'much%20ado%20about%20nothing'

    """


    # Count num of spaces based on str length 
    num_spaces = sentence.count(" ", 0, true_len)

    rep_spaces = sentence.replace(" ", "%20", num_spaces)
    urlfied = rep_spaces.replace(" ", "")
    
    return urlfied 
 

 """
 Explanation:
 


 """


##################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print


