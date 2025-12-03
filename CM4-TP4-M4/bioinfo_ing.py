#Bioinfo, créé par Iñaki Salomé-Parra

def is_adn(text):
    # pré : prendre une chaîne de caractères
    # post : définir si cette chaîne est un ADN (présence de a,c,g,t, en minuscule ou majuscule) ATTENTION, pas d'autres caractères autorisés
    if text == "":
        return False
    for caract in text:
        if caract not in ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']:
            return False
    return True

def positions(text, car):
    # pré : prise d'une chaîne de caractères et d'un motif à identifier. Marche pour tout.
    # post : renvoyer la position du motif dans la chaîne de caractères.
    l = []
    for postxt in range(len(text)):
        if text[postxt].lower() == car[0].lower():
            ident = True
            for poscar in range(1, len(car)):
                if text[postxt + poscar].lower() != car[poscar].lower():
                    ident = False
                    break
            if ident:
                l.append(postxt)
    return l #renvois d'une liste avec les positions recherchées dans la chaîne de caractères

def distance_h(text1, text2):
    #pré : prise de deux chaines de caractères. Marche même si ce n'est pas de l'ADN.
    #post: calcul de la distance de Hamming entre les deux chaînes. Renvoie None si les deux chaînes n'ont pas la même longueur
    dist = 0
    text1 = text1.lower()
    text2 = text2.lower()
    if len(text1) != len(text2):
        return None #en cas de longueur différente
    else:
        for caract2 in range(len(text2)):
            if text2[caract2] != text1[caract2]:
                dist += 1
    return dist #distance en cas de longueur indentique

def distances_matrice(l):
    #pré : prise d'une liste contenant plusieurs chaînes de caractère.
    #post : calcul des distances de Hamming entre chaque chaîne et toutes les autres. Sortie sous forme de matrice.
    l1 = []
    for i in range(len(l)):
        l[i] = l[i].lower()
        ligne = []
        for j in range(len(l)):
            m = distance_h(l[i], l[j].lower())
            ligne.append(m)
        l1.append(ligne)
    return l1