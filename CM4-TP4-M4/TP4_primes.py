#nombre premiers par le crible d'Eratosthène

def primes(max):
    l = []
    if max <=1:
        return l
    for i in range(2,max+1):
        j = 0
        premier = True
        while j <= len(l)-1:
            if i%l[j] == 0:
                premier = False
            j+=1
        if premier:
            l.append(i)
    return l