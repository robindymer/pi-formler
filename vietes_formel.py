"""
* Viete's formel för pi
"""
import math

def get_factor(n):
    if n == 1:
        return math.sqrt(1/2)
    elif n < 1:
        return "NA"
    else:
        return math.sqrt(1/2 + 1/2*get_factor(n-1))

def viete_approx(n):
    approx_pi = 1;
    for i in range(1, n+1):
        print(get_factor(i))
        approx_pi *= get_factor(i)
    return 2 / approx_pi
