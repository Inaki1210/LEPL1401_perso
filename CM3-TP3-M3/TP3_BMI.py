#indice BMI

def quetelet(height, weight):
    """
    pré : Utilise les données de taille en m et de poids en kg pour donner l'indice IMC
    post : renvoye le type de corpulence en fonction du seuil IMC
    """
    indice = weight / (height**2)
    if indice < 20:
        return 'thin'
    elif indice >= 20 and indice <= 25:
        return 'normal'
    elif indice > 25 and indice <= 30:
        return 'overweight'
    else :
        return 'obese'