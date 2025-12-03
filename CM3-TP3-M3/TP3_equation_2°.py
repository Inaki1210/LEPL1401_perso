#équations du second degré

import math
def rho(a,b,c):
    rho = b**2 - 4*a*c
    return rho

def n_solutions(a,b,c):
    if rho(a,b,c) < 0:
        return 0
    elif rho(a,b,c) == 0:
        return 1
    else:
        return 2
    
def solution(a,b,c):
    if rho(a,b,c) == 0:
        sol = -b/(2*a)
        return sol
    if rho(a,b,c) > 0:
        sol1 = (-b+math.sqrt(rho(a,b,c)))/(2*a)
        print(sol1)
        sol2 = (-b-math.sqrt(rho(a,b,c)))/(2*a)
        print(sol2)
        if sol1 < sol2:
            return sol1
        else:
            return sol2

print(rho(-6, 2, 15))
print(n_solutions(-6, 2, 15))
print(solution(-6, 2, 15))