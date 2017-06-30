
""" 
Coding challenge 06/26/16 

Given a number, return how many holes are associated with each indivial
number and return an integer with the total count 

"""
holes = {"1":0, "2":0, "3":0, "5":0, 7:0, 
        "0":1, "4":1, "6":1, "9":1,
        "8":2}

def count_holes(num):
    """
    Function counts how many holes are hit in a series of numbers
    
    >>> count_holes(0)
    1

    >>> count_holes(630)
    2

    >>> count_holes(6308)
    4

    """

    count = 0 

    num = str(num)


    for n in num:
        count += holes.get(n, 0)

    return count



################### DocTests ###########################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

