#calcul des intérêts

def interests(base, y, x):
    """
    pré : donne un montant de base, un tuax d'intérêt et une durée
    post : renvoye solde, le solde du compte épargne après un certain temps (et un certain taux)
    """
    solde = base+(base/100)*y
    for i in range (x-1):
        solde+=(solde/100)*y
    return solde

print(interests(10,4,10))