#PGCD entre deux nombres a et b

def gcd(a,b):
    gcd = 0
    if a == 0 or b == 0:
        return max(a,b)
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd
