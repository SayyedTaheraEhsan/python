import math

def fermat_factor(n):
    a = math.isqrt(n)  # floor(sqrt(n))
    if a * a < n:
        a += 1  # ceil(sqrt(n))
    while True:
        b2 = a*a - n
        b = math.isqrt(b2)
        if b * b == b2:
            return a - b, a + b
        a += 1

# Your number
n = 288230305553188811

p, q = fermat_factor(n)

print("p =", p)
print("q =", q)
print("Check:", p * q == n)
