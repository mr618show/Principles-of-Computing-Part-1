import math
def appendsums(lst): 
    """ 
    Repeatedly append the sum of the current last three elements 
    of lst to lst. 
    """
    for i in range(25):
        last_three_sum = sum(lst[-3:])
        lst.append(last_three_sum)
    print lst
sum_three = [0, 1, 2]
appendsums(sum_three)
print len(sum_three)
print sum_three[20]