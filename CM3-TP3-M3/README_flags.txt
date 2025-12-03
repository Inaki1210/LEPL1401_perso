Alexis Hariga et Iñaki Salomé-Parra
README flags.py
ATTENTION, pour une bonne exécution du programme, entrer all() dans la console, le programme se charge du reste
Nous commençons par importer turtle pour pouvoir utiliser cet outil graphique.

Paramétrage de turtle
> création de la fenêtre d'affichage
> nommage de la turtle (jeff)
> vitesse définie sur "le plus rapide"
> fond d'écran défini en rose pour avoir un contraste avec les parties blanche des drapeaux (pour ne pas faire de cadre)

1ère fonction : etoile()
> définit la façon de faire les étoiles du drapeau européen
    > définition de la couleur de trait (jaune)
    > descente du stylo pour tracer
    > demande de remplissage de la forme qui sera créée par la couleur préselectionnée
    > boucle for pour tracer une étoile:
        > avancer de 7,
        > pivoter de 72° sur la gauche
        > avancer de 7
        > pivoter de 144° sur la droite
        (permet de tracer 1/5ème du contour de l'étoile)
        (opération répétée 5 fois pour une étoile)
    > arrêt du remplissage
    > levée du stylo
    (jeff est revenu a sa position initiale avec la même direction)

2ème fonction : rectangle()
> définit le fond du drapeau européen
    > définition de la couleur du trait en bleu, descente du stylo et début du remplissage de la forme
    > boucle for définissant la 1ère moitié du fond du drapeau:
        > avancer de 170
        > pivoter de 90° sur la droite
        > avancer de 200
        > pivoter de 90° sur la droite
        (trace 1/2 rectangle. Actions répétées 2 fois pour 1 rectangle)
        (jeff est revenu a sa position et direction initiale)
    > demi tour sur la gauche pour préparer le second rectangle
    > boucle for fonctionnant de manière similaire que la précédente:
        > Avancer de 155 au lieu de 170 (différence d'une étoile en taille) pour avoir les étoiles centrées
        > pivoter à gauche de 90°
        > avancer de 200
        > pivoter à gauche de 90°
    > lever le stylo
    > arrêter le remplissage

3ème fonction : european_flag()
> définit le drapeau européen
    > pivoter de 90° sur la gauche
    > monter de 50
    > pivoter de 90° sur la droite
    (permet de décaler le fond pour avoir les étoiles au centre. Le dernier pivot initialise la position initiale pour le fond)
    > appelle la fonction rectangle() pour tracer le fond
    > retourne à la position initiale (left(90), forward(38), left(90))
    (initialise la position de départ pour les étoiles)
    > boucle for pour créer les 12 étoiles:
        > appelle la fonction étoile()
        > pivot de 15*(2*i+1)° sur la droite pour "former" un dodécagone avec les étoiles.
        (le i correspond à la variable de la boucle for. Il faut un nombre impair pour les rotations (15,45,75°,...))
        > avancer de 32
        > pivoter à gauche de 15*(2*i+1)° pour initialiser la position de départ de la prochaine étoile
    (pas de penup car la fonction étoile() le fait à chaque itération)
    (taille du drapeau : 325 par 200, soit légèrement plus que le rapport de 3/2 pour un drapeau)

4ème fonction : three_color_flag_vert(color1, color2, color3)
> fonction générique pour faire les drapeaux à 3 colonnes de couleurs
    > boucle for avec chaque couleur dans une liste:
        > sélection de la couleur, abaissement du stylo, début du remplissage de la forme
        > boucle for pour créer une bande verticale:
            > avancer de 100
            > pivoter de 90° sur la droite
            > avancer de 50
            > pivoter de 90° sur la droite
            (boucle exécutée 2 fois pour faire une bande)
        > arrêt du remplissage,levée du stylo
        > pivot sur la droite de 90°, avancée de 50
        > pivot sur la gauche de 90° pour initialiser la position initiale de la prochaine bande
        (étant donné que jeff retourne à la position initiale après chaque bande, il faut qu'il se déplace d'une largeur de bande)
    (boucle répétée 3 fois, une fois par couleur)
    (drapeau de 150 par 100)

fonction belgian_flag()
> définit le drapeau belge via three_color_flag_vert(color1, color2, color3)
(en remplaçant les couleurs par "black", "yellow", "red")
(pas utile au fond mais créée pour répondre aux demandes)

fonction three_color_flag_hor(color1, color2, color3)
>fonction similaire à three_color_flag_vert(color1, color2, color3) mais pour les bandes horizontales
    > avance de 100 et pivote de 90° sur la droite pour commencer par le haut du drapeau et non par le bas (comme pour les drapeaux verticaux)
    > boucle for avec chaque couleur dans une liste:
        > sélection de la couleur, abaissement du stylo, début du remplissage de la forme
        > boucle for pour créer une bande horizontale:
            > avancer de 150
            > pivoter de 90° sur la droite
            > avancer de 33
            > pivoter de 90° sur la droite
            (boucle exécutée 2 fois pour faire une bande)
        > arrêt du remplissage,levée du stylo
        > pivot sur la droite de 90°, avancée de 33
        > pivot sur la gauche de 90° pour initialiser la position initiale de la prochaine bande
        (étant donné que jeff retourne à la position initiale après chaque bande, il faut qu'il se déplace d'une largeur de bande)
    (boucle répétée 3 fois, une fois par couleur)
    > déplacement de 150, pivot à droite de 90°, avancée de 1, demi-tour gauche
    (nécessaire pour se retrouver à la fin du drapeau créé et à la même hauteur que le bas d'un drapeau vertical)
    (drapeau de 150 par 99)
    
fonction mvt()
> permet le déplacement de la position finale du drapeau UE à la position de départ pour les drapeaux du haut (depuis le bord de la fenêtre en plein écran)
    > levée du stylo (mesure de sécurité, redondance)
    > demi-tour gauche, avancée de 550 (pour s'éloigner en longeur de l'UE)
    > pivot de 90 et déplacement de 90 (pour s'éloigner en hauteur de l'UE)

fonction mvt_1()
> donne le déplacement entre chaque drapeaux
    > levée du stylo (mesure de sécurité, redondance)
    > pivot droit de 90°
    > avancée de deux largeur de bande verticales (soit 100)
    > pivot gauche de 90° pour initialiser la position de départ des drapeaux

fonction mvt_2()
> donne le déplacement entre le drapeau luxembourgeois et autrichien (soit entre les deux bandes de drapeaux)
    > levée du stylo (mesure de sécurité, redondance)
    > pivot gauche de 90° pour remonter la bande
    > avancée de 1150 (longueur de la bande)
    > pivot gauche de 90° puis descente de 400 (pour avoir une symétrie entre la distance du drapeau EU et des bandes)
    (la distance de 400 inclus la taille d'un drapeau de 150 car les drapeaux sont dessinés à partir du bord inférieur gauche)
    > demi-tour gauche pour initialiser la position de départ des drapeaux

fonction all()
> dessine tous les drapeaux
    > appel de european_flag() pour le drapeau de l'UE
    > mvt() pour préparer la 1ère bande de drapeaux
    > blegian_flag()pour le drapeau belge (pourrait être remplacé par three_color_flag_vert(color1, color2, color3))
    > mvt_1() pour préparer le drapeau suivant
    > three_color_flag_vert(color1, color2, color3)
        > avec les couleurs du drapeau français
    > mvt_1() pour préparer le drapeau suivant
    > three_color_flag_hor(color1, color2, color3)
        > avec les couleurs du drapeau allemand
    > enchaînement de mvt_1() et three_color_flag_hor(color1, color2, color3) pour les drapeaux hollandais et luxembourgeois
    > mvt_2() pour préparer la seconde ligne de drapeaux
    > enchaînement de mvt_1() et three_color_flag_hor(color1, color2, color3) pour les drapeaux autrichiens, bulgare, estonien, hongrois et lituanien

Il n'y a pas de wn.mainloop() car nous n'arrivons pas à l'intégrer sans empêcher le code de fonctionner.

Nous avons commencé par faire le drapeau belge et allemand dans 2 programmes séparé pour se familiariser avec turtle.
Ensuite, nous nous sommes tous les deux mis sur le projet de faire les étoiles, chacun de notre côté pour voir comment faire.
Après une mise en commun, nous avons défini la meilleur fonction étoile et avons créé le drapeau européen.
S'en est suivit une phase de création du programme pour tous les drapeaux demandé.
Nous avons ensuite optimisé le programme pour ne pas avoir une fonction par drapeau, mais une par style de drapeau
Le plus dur aura été de faire le drapeau de l'UE car il demandait de placer les étoiles sur un polygone à 12 côtés, tout en les maintenant pointes vers le haut et en gardant le polygone centré sur le fond bleu.