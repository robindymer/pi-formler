"""
* Walli's formel för pi
"""
n = 100000000 # number of iterations
# pi / 2 --> 2 is multiplied to yield pi, and then multiplied by the first term, 2/1
pi = 4
t = 2
d = 1

for i in range(n):
    if i % 2 == 0:
        d += 2
    else:
        t += 2
    # print(str(t) + '/' + str(d))
    pi *= (t / d)
