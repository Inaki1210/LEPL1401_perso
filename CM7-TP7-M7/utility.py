#Utility

import search

print("Programme créé par Iñaki Salomé-Parra, groupe 11.97 (oui oui, j'ai rajouté une ligne ;)")
filename = input ("Spécifiez le nom de fichier: ")
index = search.create_index ( filename )
loop = True
while loop:
    words = input ("Spécifiez les mots a rechercher, en utilisant des espaces entre les mots: ")
    lines = search.get_lines ( words.strip().split(), index )
    print("Les mots se retrouvent dans ces lignes:")
    for line in lines: #je comprends pas trop ce qui est fait ici....
        print(line)
    encore = input("Voulez-vous continuer les recherches ? [y/n]").lower
    if encore == 'n':
        loop == False
    elif encore != 'n' or encore != 'y':
        print("Ok, je considère que tu veux t'arrêter...")
        loop = False