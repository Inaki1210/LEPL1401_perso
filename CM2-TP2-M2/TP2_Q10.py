is_prime = True
n = 97           #Un entier supérieur à 1

for i in range(2,n):
    if n%i ==0:
        is_prime = False
print(is_prime)