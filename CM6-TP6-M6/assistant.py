#mission 6, assistant
# Programme créé par Hélène Dodrémont et Iñaki Salomé-Parra, groupe 11.97

def file(filename):
    """
    Permet d'ouvrir le fichier 'filename'

    args:
        filename, un string contenant le nom du fichier à ouvrir
    
    returns:
        Si le fichier existe, renvoye "Fichier filename chargé" et le stock dans la variable file
        Sinon, renvoye "Le fichier filename n'est pas trouvé"
    """
    try:
        file = open(filename,"r")
        file.read()
        print('Fichier', filename,'chargé',"\n")
    except:
        print("Le fichier",filename,"n'est pas trouvé","\n")

###

def info():
    """
    Permet de connaitre le nombre de lignes et de caractères d'un fichier

    args:
        file, le fichier chargé par la fonction file(filename).

    Returns:
        count_l, le nombre de lignes
        count_c, le nombre de caractères
        "Le fichier filename n'est pas chargé" si filename n'a pas encore été chargé.
    
    """
    try:
        count_l = 0
        count_c = 0
        file = open(filename,"r")
        for line in file:
            count_l+=1
            count_c+=len(line)
        print(count_l , "lignes","\n")
        print(count_c , 'caractères',"\n")
    except:
        print("Le fichier", filename ,"n'est pas chargé.","\n")

###

def words():
    """
    Créée une liste à partir du fichier filename. Chaque élément est un mot.

    Args: 
        filename, le fichier chargé par la fonction file(filename)

    Returns:
        w, la liste triée créée à partir du fichier
        "Lecture du fichier comme une liste de mots (dictionnaire)", si la fonction words() fonctionne bien
        "Le fichier", filename, "n'est pas chargé, impossible d'effectuer words()."
    """
    try:
        file = open(filename,"r")
        f = []
        for line in file:
            f.append(line.split(','))
        w = []
        for word in f:
            w.append(word[0])
        w = sorted(w)
        print('Lecture du fichier comme une liste de mots (dictionnaire)',"\n")
        return w
    except:
        print("Le fichier", filename, "n'est pas chargé, impossible d'effectuer words().","\n")

###

def search(word,filename):
    """
    Recherche un mot dans une liste provenant d'un fichier (via words()) et indique s'il y est

    Args:
        word , le mot recherché
        filename, le fichier dans lequel il faut chercher
    
    Returns:
        Retourne 'word, est dans le fichier' s'il y est
        'word, n'est pas dans le fichier' sinon
    """
    l = words()
    first = 0
    last = len(l)
    found = False

    while first <= last and not found:
        middle = (first + last)//2
        if l[middle] == word:
            found = True
        else:
            if word < l[middle]:
                last = middle - 1
            else:
                first = middle + 1
    if found == True:
        print(word," est dans le fichier","\n")
    else:
        print(word," n'est pas dans le fichier","\n")

###

def sum(numbers):
    """
    Calcule la somme des éléments d'une liste

    Args : 
        numbers, une liste comprenant les différents nombres

    Returns:
        sum, la somme de la liste
        "Merci d'ajouter des [] lorsque vous renseignez votre liste." s'il n'y a pas de listes
    """
    try:
        sum = 0
        for i in numbers:
            if numbers == []:
                print("La liste est vide. La somme n'existe pas.","\n")
            if type(i) == int or type(i) == float:
                sum+=i
        print(sum)
    except:
        print("Merci d'ajouter des [] lorsque vous renseignez votre liste.","\n")

###

def avg(numbers):
    """
    Cacule la moyenne arithmétique d'une liste

    Args:
        numbers, la liste des nombres à prendre en compte

    Returns:
        avg, la moyenne arithmétique de la suite
        "Erreur. Merci de renseigner des nombres et ne pas renseigner une liste vide. N'oubliez pas les []."
            si la fonction ne parvient pas à calculer la moyenne

    """
    try:
        if numbers == []:
            print("La liste est vide, moyenne impossible","\n")
        sum = 0
        for i in numbers:
            if type(i) == int or type(i) == float:
                sum+=i
        avg = sum/(len(numbers))
        print(avg,"\n")
    except:
        print("Erreur. Merci de renseigner des nombres et ne pas renseigner une liste vide. N'oubliez pas les [].","\n")

###

def help():
    """
    Donne une liste de commandes utilisables

    Args : 
    //

    Returns: 
    La liste de commande avec leurs descriptions
    """
    print("""Voici la liste des instructions possibles:
          file('name'), permet d'ouvrir un fichier. Essentiel pour les fonctions infos, words, search
          info(), donne le nombre de lignes et de caractères dans le fichier ouvert par file('name')
          words(), créée une liste ordonnée de mots à partir du fichier ouvert par file('name')
          search('word',words) permet de chercher un mot dans une liste de mots words. Nécessite de lancer file('name') et words() avant
          sum(numbers) renvoie la somme d'une liste de nombres
          avg(numbers) renvoie la moyenne algébrique d'une liste de nombres
          """)

###

def exit():
   """
   Retourne un message de fermeture du programme

   Args:
    //

   Returns:
    "Fin du programme"
   """
   print("Fin du programme","\n") 

###

def search_comm(command):
    """
    Permet de rechercher une fonction dans une liste de fonctions.

    Args:
        command, la fonction recherchée par l'utilisateur, sans les ()

    Returns:
        Renvoie True si la fonction est dans la liste de fonctions
        Renvoie False sinon
    """
    l = ["file","info","words","search","sum","avg","help","exit"]
    l = sorted(l)
    first = 0
    last = len(l)
    found = False

    while first <= last and not found:
        middle = (first + last)//2
        if l[middle] == command:
            found = True
        else:
            if command < l[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

###

loop = True
print("Programme créé par Hélène Dodrémont et Iñaki Salomé-Parra, Groupe 11.97")
print("Si vous ne savez pas quoi effectuer, entrez help","\n")

while loop:
    """
    Boucle permettant de faire tourner l'assistant de manière continue, sauf si loop == False
    Permet d'exécuter les fonctions demandées, si elles sont dans le programme.
    """

    command = input("Entrez la commande que vous voulez exécuter: ").lower()
    if search_comm(command) == False:
        print("Merci de renseigner une fonction valide. Si vous avez besoins d'aide, entrez 'help'","\n")
    else:

        if command == "file":
            filename = input("Merci de renseigner le fichier que vous voulez charger: ")
            file(filename)

        if command == "info":
            try:
                quest = input(str("Doit-on utilisé le fichier chargé dans file ? ([Y/n]) ")).lower()
                if quest == 'Y':
                    info()
                else:
                    filename = str(input("Merci de renseigner le fichier à ouvrir: "))
                    file(filename)
                    info()
            except:
                print("Le fichier n'est pas chargé","\n")
        
        if command == "words":
            try:
                quest = input(str("Doit-on utilisé le fichier chargé dans file ? ([Y/n]) ")).lower()
                if quest == 'Y':
                    words()
                else :
                    filename = str(input("Merci de renseigner le fichier à ouvrir: "))
                    file(filename)
                    words()
            except:
                print("Le fichier n'est pas chargé","\n")
        
        if command == "search":
            try:
                word = input(str("Merci de renseigner le mot que vous recherchez: "))
                quest = input(str("Doit-on utilisé le fichier chargé dans file ? ([Y/n]) ")).lower()
                if quest == 'Y':
                    search(word, filename)
                else :
                    filename = str(input("Merci de renseigner le fichier à ouvrir: "))
                    file(filename)
                    words()
                    search(word,filename)
            except:
                print("Le fichier n'est pas chargé","\n")

        if command == "sum":
            lst = input("Merci de renseigner la liste des nombres à prendre en compte, sans oublier [ au début et ] à la fin")
            sum(lst)

        if command == "avg":
            lst = input("Merci de renseigner la liste des nombres à prendre en compte, sans oublier [ au début et ] à la fin")
            avg(lst)

        if command == "help":
            help()

        if command == "exit":
            exit()
            loop = False