#trouver la médiane M de trois nombre a,b et c
#Etant donné que la médiane d'une série impaire correspond à la valeur du mileu,
#il suffit de trouver la valeur intermédiaire

a = 81    #définition de a,b et c
b = 43
c = 39
if b <= a and a <= c or c <= a and a <= b: #cas 1 ou a est la médiane. deux sous cas : b<c et c<b
    print(a)
    
elif a <= b and b <= c or c <= b and b <= a : #cas 2 ou b est la médiane. deux sous cas : a<c et c<a
    print(b)
    
else: #dernier cas. c est d'office la médiane (cas d'une série impaire).
    print(c)