"""
* Formel för pi baserad på taylorserien för derivatan av arcsin
"""
import math

def walter_approx(n):
    pi = 1
    for i in range(1, n+1):
        nu = 1
        if i >= 2:
            for j in range(2, i+1):
                nu *= (j*2-1)**2
        de = math.factorial(i*2+1)
        # print('Loop: ' + str(i))
        # print(nu) # not 9
        # print(de) # correct
        pi += nu / de
    return pi
