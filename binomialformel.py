"""
* En formel för pi baserad på binomialutveckling av sqrt(1-x^2)
"""
import math

def combinatorics(n, k):
    current = n
    for i in range(1, k):
        current *= (n-i)
    return (current / math.factorial(k))

def piApprox(n):
    almostPi = 1
    for i in range(1, n):
        almostPi -= abs(combinatorics(0.5, i) * 1/(2*i+1))
    return almostPi*4
