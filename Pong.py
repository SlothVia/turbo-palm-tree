# Simple pong

import turtle  # Module pour le programmation de jeux basics
import winsound 

win = turtle.Screen()  # Faire un ecran
win.title("Pong")  # Donner un titre à le fenetre
win.bgcolor("black")  # Choisir une couleur pour le fond
win.setup(width=800, height=600)  # Mettre en place les dimensions de la fenetre
win.tracer(0)


    
    

# Paterne A à droite 
paterne_a = turtle.Turtle()  # Créer un object de type Turtle
paterne_a.speed(0)
paterne_a.shape("square")  # Choisir la forme de l'objet
paterne_a.color("white")  # Choisir la couleur de l'objet
paterne_a.shapesize(stretch_wid=5, stretch_len=1)  # Changer la dimension de l'objet | changer la largeur à 5 et la longeur = 1 
paterne_a.penup()
paterne_a.goto(-350, 0)  # Définir la position initiale de l'objet


# Paterne B à gauche
paterne_b = turtle.Turtle()  # Créer un object de type Turtle
paterne_b.speed(0)
paterne_b.shape("square")
paterne_b.color("white")
paterne_b.shapesize(stretch_wid=5, stretch_len=1)
paterne_b.penup()
paterne_b.goto(350, 0)


# Balle

balle = turtle.Turtle()  # Créer un object de type Turtle
balle.speed(0)
balle.shape("square")
balle.color("white")
balle.penup()
balle.goto(0, 0)
balle.dy =  0.07 #La boule va avancer par deux pixels dans l'axe vertical positif
balle.dx =  0.07 #La boule va avancer par deux pixels dans l'axe horizontal positif


#Score variable
score_a = 0 
score_b = 0




#Score 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() # Pour empêcher de créer des lignes 
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B : 0", align = "center", font =("Courier", 24, "normal"))


# Player_a = turtle.Turtle()
# Player_a.goto(-50,370 )
# Player_a.title("Player A")

# Fonctions

def paterne_a_up():  
    y = paterne_a.ycor() 
    y += 20
    paterne_a.sety(y)

    
def paterne_a_down(): 
    y = paterne_a.ycor()  
    y -= 20
    paterne_a.sety(y)

    
def paterne_b_up():  
    y = paterne_b.ycor()  
    y += 20
    paterne_b.sety(y)

    
def paterne_b_down(): 
    y = paterne_b.ycor()  
    y -= 20
    paterne_b.sety(y)

    
# Touches du clavier 

win.listen()
win.onkeypress(paterne_a_up, "z")
win.onkeypress(paterne_a_down, "s")
win.onkeypress(paterne_b_up, "Up")
win.onkeypress(paterne_b_down, "Down")


# Main game loop 

while True:
    win.update()  # Faire une boucle  et mettre à jour la fenetre à chaque fois
    
    
    #Dplacement de la balle
    balle.setx(balle.xcor() + balle.dx)
    balle.sety(balle.ycor() + balle.dy)
    
    
    
    #Bord de l'écran 
    if balle.ycor() > 290: 
        balle.sety(290)
        balle.dy *= -1  #Changer la position de la balle quand elle attendra le hauut de la fenetre
        #winsound.PlaySound("SystemHand", winsound.SND_ASYNC)
        
     
    if balle.ycor() < -290: 
        balle.sety(-290)
        balle.dy *= -1
        
    
    if balle.xcor() > 390: 
        balle.goto(0, 0)
        balle.dx *= -1
        score_a += 1
        pen.clear()  
        pen.write("Player A: {}  Player B : {}".format(score_a, score_b), align = "center", font =("Courier", 24, "normal"))    
       
    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dx *= -1   
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}  Player B : {}".format(score_a, score_b), align = "center", font =("Courier", 24, "normal"))
        
        
    #Rebond de la balle sur les paternes
    
    if (balle.xcor() > 340  and balle.xcor() < 350) and (balle.ycor() < paterne_b.ycor() + 40 and balle.ycor() > paterne_b.ycor() - 40) :
        balle.setx(340)
        balle.dx *= -1
        
        
    if (balle.xcor() < -340  and balle.xcor() > -350) and (balle.ycor() < paterne_a.ycor() + 40 and balle.ycor() > paterne_a.ycor() - 40) :
        balle.setx(-340)
        balle.dx *= -1
