
# Coding challenge 06/26/16 

holes = {"1":0, "2":0, "3":0, "5":0, 7:0, 
        "0":1, "4":1, "6":1, "9":1,
        "8":2}

def countHoles(num):

"""
Function counts how many holes are hit in a series of numbers
"""

    count = 0 

    num = str(num)


    for n in num:
        count += holes.get(n, 0)

    return count


test = countHoles(630)
print test 