#créé par Alexis Hariga et Iñaki Salomé-Parra (groupe 11.97)
#drapeau de l'Union Européenne et de certains drapeaux de pays membres
#ATTENTION, pour une bonne exécution du programme, entrer all() dans la console, le programme se charge du reste
import turtle

wn = turtle.Screen()
jeff = turtle.Turtle() #tortue nommée jeff
jeff.speed("fastest") #tortue rapide
wn.bgcolor("pink") #choix d'un fond rose pour faire ressortir les parties blanches d'un drapeau

print("Ce programme a été créé par Alexis Hariga et Iñaki Salomé-Parra du groupe 11.97")
print("Merci de mettre la fenêtre de turtle en plein écran pour voir tous les drapeaux")

def etoile(): #fonction traçant les étoiles du drapeau EU
    jeff.color("yellow") #étoiles en jaune
    jeff.pendown()
    jeff.begin_fill()
    for h in range(5): #traçage d'une étoile
        jeff.forward(7)
        jeff.left(72)
        jeff.forward(7)
        jeff.right(144)
    jeff.end_fill()
    jeff.penup()
    
def rectangle(): #fonction traçant le fond du drapeau EU
    jeff.color("blue") #fond en bleu
    jeff.pendown()
    jeff.begin_fill()
    for i in range(2): #1ère moitié du fond
        jeff.forward(170)
        jeff.right(90)
        jeff.forward(200)
        jeff.right(90)
    jeff.left(180)
    for j in range(2): #seconde moitié du fond
        jeff.forward(155)
        jeff.left(90)
        jeff.forward(200)
        jeff.left(90)
    jeff.end_fill()
    jeff.penup()

def european_flag(): #création du drapeau de l'UE au complet
    jeff.left(90) 
    jeff.forward(50)
    jeff.right(90)
    rectangle() #insertion du fond
    jeff.left(90)
    jeff.forward(38)
    jeff.left(90)
    for k in range(12):
        etoile() #ajout des 12 étoiles
        jeff.right(15*(2*k+1))
        jeff.forward(32)
        jeff.left(15*(2*k+1))

def three_color_flag_vert(color1, color2, color3): #définition d'un drapeau a trois bandes verticales et trois couleurs
    for i in (color1,color2,color3): #création de chaques bandes de couleur
        jeff.color(i)
        jeff.pendown()
        jeff.begin_fill()
        for j in range(2): #création d'une bande
            jeff.forward(100)
            jeff.right(90)
            jeff.forward(50)
            jeff.right(90)
        jeff.end_fill()
        jeff.penup()
        jeff.right(90)
        jeff.forward(50)
        jeff.left(90)

def belgian_flag(): #création du drapeau belge en fonction de la fonction ci-dessus. Elle n'est pas utile mais demandée.
    three_color_flag_vert("black","yellow","red")

def three_color_flag_hor(color1,color2,color3): #définition d'un drapeau a trois bandes horizontales et trois couleurs
    jeff.forward(100)
    jeff.right(90)
    for i in(color1,color2,color3): #création de chaque bande en fonction d'une couleur
        jeff.color(i)
        jeff.pendown()
        jeff.begin_fill()
        for j in range(2): #création d'une bande
            jeff.forward(150)
            jeff.right(90)
            jeff.forward(33)
            jeff.right(90)
        jeff.end_fill()
        jeff.penup
        jeff.right(90)
        jeff.forward(33)
        jeff.left(90)
        
    jeff.forward(150)
    jeff.right(90)
    jeff.forward(1)
    jeff.left(180)

def mvt(): #déplacement entre le drapeau EU et le premier drapeau
    jeff.penup()
    jeff.left(180)
    jeff.forward(550)
    jeff.right(90)
    jeff.forward(90)
    
def mvt_1(): #déplacement entre chaque drapeau non EU
    jeff.penup()
    jeff.right(90)
    jeff.forward(2*50)
    jeff.left(90)

def mvt_2(): #déplacement entre le dernier drapeau de la ligne supérieure et le premier drapeau de la ligne inférieure
    jeff.penup()
    jeff.left(90)
    jeff.forward(1150)
    jeff.left(90)
    jeff.forward(400)
    jeff.left(180)

def all(): #création de tous les drapeaux grâces aux fonction
    european_flag() #drapeau de l'UE
    mvt() #déplacement jusqu'au 1er enplacement de drapeau
    belgian_flag() #drapeau belge
    mvt_1() #déplacement vers le second drapeau
    three_color_flag_vert("blue","white","red") #drapeau français
    mvt_1() #déplacement vers le 3ème drapeau
    three_color_flag_hor("black","red","yellow") #drapeau allemand
    mvt_1() #idem que les autres mvt_1()
    three_color_flag_hor("red","white","blue") #drapeau Hollandais
    mvt_1()
    three_color_flag_hor("red","white","cyan") #drapeau luxembourgeois
    mvt_2() #déplacement vers la seconde ligne de drapeau (sous EU)
    three_color_flag_hor("red","white","red") #drapeau autrichien
    mvt_1()
    three_color_flag_hor("white","green","red") #drapeau bulgare
    mvt_1()
    three_color_flag_hor("blue","black","white") #drapeau Estonie
    mvt_1()
    three_color_flag_hor("red","white","green") #drapeau Hongrois
    mvt_1()
    three_color_flag_hor("yellow","green","red") #drapeau Lituanie

all()