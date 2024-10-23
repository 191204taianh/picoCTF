#n=p*q
#x=p+q

#n=p(x-p)
#n=px-p^2
#p^2-px+n=0

#a=1,b=-x,c=n

#Solve for p: (-b+sqrt(b^2-4ac))/2a
#Solve for q: (-b-sqrt(b^2-4ac))/2a

import gmpy2
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y & x:
       x = y
       y = (x + n // x) // 2
    return xp=(x+isqrt(x**2-4*n))//2
q=(x-isqrt(x**2-4*n))//2
print(p)
print(q)
print(p*q==n)

e = 65537

m = gmpy2.lcm(p - 1, q - 1)
d = pow(e, -1, m)

plain = pow(c, d, n)
print(f'plain = {plain:x}')