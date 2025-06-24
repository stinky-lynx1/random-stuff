import math # just in case 

a, b, dx, i, r, func= float(input("Upper bound a=")), float(input("Lower bound b=")), float(input("Variable dx=")), 0, int(input("Digits after decimal point n=")), input("f(x)=")

x1 = b
while x1 <= a:
    c = lambda x : eval(func)
    y = c(x1)
    print("y=" + str(y), "x=" + str(x1))
    i += y * dx
    x1 += dx

print("The integral for your function and parameters is f(x)=" + str(round(i,r)))
