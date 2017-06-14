"""
Write a method to replace all spaces in a string with '%20'. 

NOTE: For those solving problem in Java, you may assume that 
the string has sufficient space at the end to hold the additional characters, and
that you are given the "true" length of the string. 

"""

# FIRST TRY: Using a built-in method 

def urlify(sentence):

    no_words = len(sentence.split()) - 1

    urlfied = sentence.replace(" ", "%20", no_words)

    testing = len(urlfied)
    print testing

    return urlfied 


test1 = urlify("Mr John Smith   ")
print test1 
# Mr%20John%20Smith
