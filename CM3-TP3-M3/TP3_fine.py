#calcul des amendes pour excès de vitesse


def fine(authorized_speed, actual_speed):
    """
    pré : prend la vitesse limite autorisée et la vitesse actuelle pour calculer le montant d'une amende
    post : renvoye le montant de l'amende (0 si aucun excès, 12.5 si <2, 5*excès si moins de 10km/h et 5*excès*2 si plus de 10)
    """
    dif_speed = actual_speed - authorized_speed
    if dif_speed <= 0:
        return 0
    elif dif_speed <= 2:
        return 12,5
    elif dif_speed <= 10:
        money = dif_speed*5
        return money
    else : 
        money = (dif_speed*5)*2
        return money
    
print(fine(30,32))
print(fine(30,36))
print(fine(30, 42))