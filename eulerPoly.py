"""
参考：
https://blog.logicky.com/2017/02/07/python3-%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3/
"""
import sympy 

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n >= 1:
        factors.append(n)
    return factors

x = sympy.Symbol('x')
def eulerPoly(x, n):
    print('n:' + str(n))
    poly = x**2 + x + n
    for i in range(n - 1):
        sub = poly.subs(x, i)
        print(prime_factors(poly.subs(x, i)))
    print('\r')         

"""
print(prime_factors(12))
print(prime_factors(39))
print(prime_factors(41))
print(prime_factors(3826))
"""

eulerPoly(x, 17)
eulerPoly(x, 18)
eulerPoly(x, 40)
eulerPoly(x, 41)

