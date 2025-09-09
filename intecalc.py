from math import *  # for user-implemented functions
from time import *  # for timer

a, x1, dx, r, func = (
    float(input("Upper bound a=")),
    float(input("Lower bound b=")),
    float(input("Variable dx=")),
    int(input("Digits after decimal point n=")),
    input("f(x)="),
)

if a < x1:
    print("Integral uncalculable! Upper bound must be bigger than lower bound!")
elif a == x1:
    print("Integral uncalculable! Upper and lower bounds must have a different value!")
else:
    def integrate(a, x1, dx, r, func):
        i, cx = 0, 0
        tstart = time()
        while x1 <= a:
            c = lambda x: eval(func)  # necessary evil
            y = c(x1)
            i += y * dx
            print("y=" + str(y), "x=" + str(x1))
            cx += 1
            x1 += dx
        tend = time()
        tdelta = tend - tstart
        print(
            "The integral for your function and parameters is f(x)="
            + str(round(i, r))
            + ", calculated in "
            + str(tdelta)
            + " seconds and "
            + str(cx)
            + " cycles."
        )
