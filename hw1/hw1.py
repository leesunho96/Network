def fact(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i

    return fact

def comb(N, r):
    sum = fact(N) / fact (r) / fact(N - r)

    return sum

def sigma(n, p):
    temp = 0
    k = 20

    for r in range(0, k + 1):
        temp += comb(n, r) * (p ** r) * ((1 - p) ** (n - r))

    return temp

for i in range(50, 71):
    print('%d, %0.3f'%(i, sigma(i, 1/5)))