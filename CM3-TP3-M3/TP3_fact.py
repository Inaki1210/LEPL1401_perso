#factorielle d'un nombre n

n = int(input("met ton nombre salope : "))
def fact(n):
    sum = 1
    if n==0:
        return 1
    for i in range(1,n+1):
        sum*=i
    return sum

print(fact(n))
