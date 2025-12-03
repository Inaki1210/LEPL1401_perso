#calcul de la somme des éléments d'une liste

def sum(list):
    sum = 0
    if list == []:
        return None
    for i in list:
        if type(i) == int or type(i) == float:
            sum+=i
    return sum

print(sum([89, 25, 12, 71, 93, 6, 17, 98, 95, 31, 93, 84, 87, 28, 37, 15, 4, 93, 69, 'e']))