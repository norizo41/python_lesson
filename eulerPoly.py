"""
参考：
https://blog.logicky.com/2017/02/07/python3-%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3/
"""
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

print(prime_factors(12))
print(prime_factors(39))
print(prime_factors(41))
print(prime_factors(3826))

