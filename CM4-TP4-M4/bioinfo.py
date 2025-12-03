#Bioinfo, créé par Iñaki Salomé-Parra

print("Programme créé par Iñaki Salomé-Parra, Groupe 11.97")

nb_c =  int(input("Merci de bien vouloir donner le nombre de chaînes dont il faut calculer la distance de Hamming. ATTENTION, il faut que ces chaînes soient de l'ADN. "))
l = []
for x in range(nb_c):
    l.append(input(f"Insérez votre {x+1} ième chaîne de caractère à considérer. Il ne faut pas ajouter de guillemets ou (''). ")) #j'avoue m'être aidé d'internet pour insérer le x+1 ième terme :/

def is_adn(text):
    # pré : prendre une chaîne de caractères
    # post : définir si cette chaîne est un ADN (présence de a,c,g,t, en minuscule ou majuscule) ATTENTION, pas d'autres caractères autorisés
    if text == "":
        return False
    for caract in text:
        if caract not in ['a', 'c', 'g', 't', 'A', 'C', 'G', 'T']:
            return False
    return True

def minuscule(text):
    # pré : prendre un ADN (au préalablement vérifier donc non vérifié dans cette fonction) avec majuscules et minuscules
    # post : mettre tous les caractères majuscules en minuscule et laisser les minuscules
    rst = ''
    for caract1 in text:
        if caract1 == 'A':
            rst += 'a'
        elif caract1 == 'C':
            rst += 'c'
        elif caract1 == 'G':
            rst += 'g'
        elif caract1 == 'T':
            rst += 't'
        else:
            rst += caract1
    return rst #sortie de la chaîne en full minuscules

def position(text, car):
    # pré : prise d'une chaîne de caractères et d'un motif à identifier. Marche pour tout.
    # post : renvoyer la position du motif dans la chaîne de caractères.
    l = []
    for postxt in range(len(text)):
        if text[postxt] == car[0]:
            ident = True
            for poscar in range(1, len(car)):
                if text[postxt + poscar] != car[poscar]:
                    ident = False
                    break
            if ident:
                l.append(postxt)
    return l #renvois d'une liste avec les positions recherchées dans la chaîne de caractères

def distance_h(text1, text2):
    #pré : prise de deux chaines de caractères. Marche même si ce n'est pas de l'ADN.
    #post: calcul de la distance de Hamming entre les deux chaînes. Renvoi None si les deux chaînes n'ont pas la même longueur
    dist = 0
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
    adn_valid = 0
    for i in range(len(l)):
        if is_adn(l[i]):
            l[i] = minuscule(l[i])
            adn_valid+= 1
            ligne = []
            for j in range(len(l)):
                m = distance_h(l[i], minuscule(l[j]))
                ligne.append(m)
            l1.append(ligne)
            
    if adn_valid == 0:
        return "Mouais... on avait demandé de l'ADN... Pour la peine, pas de distance de Hamming"
    
    return l1

print(distances_matrice(l), "j'espère qu'il aura répondu à tes attentes")