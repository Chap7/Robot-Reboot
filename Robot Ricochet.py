import random
import tkinter as tk
from tkinter import PhotoImage
root = tk.Tk()

"""
    2 PARTICIPANTS :
    
Alex Khau
Front : -Création du canva (avec implémentation d'images)
        -Création des murs
        -Message gagnant, résultat du score joueur
        -Historique des déplacements

Back :  -Création d'un tableau [False, False, False, False], True si un mur est présent
        -Attribution de coordonées au tableau


Morgan Keita 
Back :  -Debug
        -Gestion des mouvements des balles
        -Gestion des collisions des balles entre elles
        -Gestion des points d'arrivés
        -Gestion du boutton restart
        -Gestion du compteur du nombre de coup
        -Fixation des balles
"""


#CREATION CANVAS

#grille
HAUTEUR = 700
LARGEUR = 700
#canva
HAUTEUR1 = 1500
LARGEUR1 = 1500

cote = 44 #modif temporaire pour debug
NB_COL = 16
NB_LINE = 16
selected_ball = None
compteur = 0
goal_pos = [(1, 3), (4, 1), (5,5),(9,2),(13,1),(3,6),(4,9),(1,10),(2,14),(4,12),(6,13),(10,12),(12,13),(11,10),(13,11),(14,6),(9,2),(10,6)]
goal_act = [-1, -1, ""]
canvas = tk.Canvas(bg = "white", width = LARGEUR1, height = HAUTEUR1)

message_victoire = canvas.create_text(1200, 200, text="")
message_result = canvas.create_text(1150, 180 ,text = "", font='Arial 16 italic', fill = 'blue')

fleche_liste = []
fleche_img_liste = {
    "bd": PhotoImage(file='flechebleu_bas.ppm'),
    "br": PhotoImage(file='flechebleu_droite.ppm'),
    "bl": PhotoImage(file='flechebleu_gauche.ppm'),
    "bu": PhotoImage(file='flechebleu_haut.ppm'),

    "rd": PhotoImage(file='flecherouge_bas.ppm'),
    "rr": PhotoImage(file='flecherouge_droite.ppm'),
    "rl": PhotoImage(file='flecherouge_gauche.ppm'),
    "ru": PhotoImage(file='flecherouge_haut.ppm'),

    "yd": PhotoImage(file='flechejaune_bas.ppm'),
    "yr": PhotoImage(file='flechejaune_droite.ppm'),
    "yl": PhotoImage(file='flechejaune_gauche.ppm'),
    "yu": PhotoImage(file='flechejaune_haut.ppm'),
    
    "gd": PhotoImage(file='flechevert_bas.ppm'),
    "gr": PhotoImage(file='flechevert_droite.ppm'),
    "gl": PhotoImage(file='flechevert_gauche.ppm'),
    "gu": PhotoImage(file='flechevert_haut.ppm'),
}

root.title("Robot Reebot")
# colonne 10, 6/7 11/12
                                                    #0 = haut, 1 = bas, 2 = droite, 4 = gauche                                                              #0 = haut, 1 = bas, 2 = droite, 4 = gauche                      #0 = haut, 1 = bas, 2 = droite, 4 = gauche                          #0 = haut, 1 = bas, 2 = droite, 4 = gauche          #0 = haut, 1 = bas, 2 = droite, 4 = gauche                                  #0 = haut, 1 = bas, 2 = droite, 4 = gauche
#creation d'un tableau
tableau = [[[True,False,False,True],[True,False,True,False],[True,False,False,True],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,True,False],[True,False,False,True],[True,False,False,False],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,True,True],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False]],
            [[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False]],
            [[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,True,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,False,False,False],[True,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[True,False,True,False],[False,False,False,True],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,True,True,False]],
            [[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,True,False,True],[False,True,False,False],[True,True,False,False],[False,True,True,False],[False,True,False,True],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,True,False],[False,True,False,True],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,True,False]]]

def check_ball(x, y, balls):
    if x > 6 and x < 9 and y > 6 and y < 9:
        return True
    for ball in balls:
        if (x, y) == ball["position"]:
            return True
    return False
    

def create_balls(colors):
    balls = []
    n_balls = len(colors)
    for i in range(n_balls):
        if (colors[i] == "blue"):
            x, y = 10, 12
        if (colors[i] == "red"):
            x, y = 11, 2
        if (colors[i] == "yellow"):
            x, y = 4, 8
        if (colors[i] == "green"):
            x, y = 6, 5
        balls.append({
            "position": (x,y),
            "color": colors[i]
        })
        print("postion = ", x, y, " color = ", colors[i])

    return balls

colors = ["red", "blue", "green", "yellow"]
balls = create_balls(colors)

def show_balls(tableau, balls):
    for ball in balls:
        i,j = ball["position"]
        color = ball["color"]
        canvas.create_oval((i * cote)+5, (j * cote)+5, (cote * (i + 1))-5, (cote * (j + 1))-5, fill=color, outline = "white")

def erase_balls(tableau, i, j): # effacer la position 
    canvas.create_oval((i * cote)+5, (j * cote)+5, (cote * (i + 1))-5, (cote * (j + 1))-5, fill="white", outline = "white")
    if i == goal_act[0] and j == goal_act[1]:
        canvas.create_rectangle((i * cote)+3, (j * cote)+3, (cote * (i + 1))-3, (cote * (j + 1))-3, fill=goal_act[2][0], outline = "white")

#creation des rectangles

color_rectangle_blue = ["blue"]

def pick_goal(): #voir comment random marche
    global goal_act
    global colors
    global goal_pos

    x,y = random.choices(goal_pos)[0]
    color = random.choices(colors)
    goal_act[0] = x
    goal_act[1] = y
    goal_act[2] = color


def show_goal():
    global goal_act
    print("SHOW GOAL ")
    i = goal_act[0]
    j = goal_act[1]
    color = goal_act[2]
    canvas.create_rectangle((i * cote)+3, (j * cote)+3, (cote * (i + 1))-3, (cote * (j + 1))-3, fill=color, outline = "white")

def erase_goal():
    global goal_act
    i = goal_act[0]
    j = goal_act[1]
    canvas.create_rectangle((i * cote)+3, (j * cote)+3, (cote * (i + 1))-3, (cote * (j + 1))-3, fill="white", outline = "white")

def reset(tableau, win):
    global balls
    global compteur
    #efface les boules
    for ball in balls:
        erase_balls(tableau, ball["position"][0], ball["position"][1])
    #efface le goal
    erase_goal()
    #recrée les boules
    balls = create_balls(colors)
    #affiche les boules:
    show_balls(tableau, balls)
    #recrée le goal
    if (win):
        pick_goal()
    show_goal()
    compteur = 0

#coordonée de chaque cases
def coord_carre(y, x): #inverse 
    x0,y0 = cote*x, cote*y
    x1,y1 = cote*(x+1), cote*(y+1)
    return [[x0,y0],[x1,y1]]

#création d'un quadrillage purement visuel sur un canva
def quadrillage():
    y = 0
    while y <= HAUTEUR :
        canvas.create_line(0, y, HAUTEUR, y, fill = "black")
        y += cote
    x = 0
    while x <= LARGEUR :
        canvas.create_line(x, 0, x, LARGEUR, fill = "black")
        x += cote

#Attribuer chaque elements du tableau à chaque case du quadrillage avec des coordonées

def placer_case(tableau): #inverse
    for y in range(len(tableau)):
        for x in range(len(tableau[y])):
            tableau[y][x].append(coord_carre(y,x))
    return tableau

#génération de murs si True
def creer_mur(tableau): # je dois check canvas create line, a quoi sert coord point 1 et 2 ? 
    # Pour chaque ligne
    for i in range(len(tableau)):
        # Pour chaque case de chaque ligne
        for j in range(len(tableau[i])):
            coord_point_1 = tableau[i][j][4][0]
            coord_point_2 = tableau[i][j][4][1]
            # On teste si il y a un mur au nord
            if tableau[i][j][0] == True:
                canvas.create_line(coord_point_1[0],coord_point_1[1],coord_point_2[0],coord_point_1[1], fill = "red",width = 8)
            # On teste si il y a un mur au sud
            if tableau[i][j][1] == True:
                canvas.create_line(coord_point_1[0],coord_point_2[1],coord_point_2[0],coord_point_2[1], fill = "red",width = 8)
            # On teste si il y a un mur au est
            if tableau[i][j][2] == True:
                canvas.create_line(coord_point_2[0],coord_point_1[1],coord_point_2[0],coord_point_2[1], fill = "red",width = 8)
           # On teste si il y a un mur au ouest
            if tableau[i][j][3] == True:
                canvas.create_line(coord_point_1[0],coord_point_1[1],coord_point_1[0],coord_point_2[1], fill = "red",width = 8)
    return None

# Gestion des events


#     walls_dir = {"Right": 2, "Left": 3, "Up": 0, "Down": 1}

def move_right(ball_y, ball_x): # inverse
    x, y = ball_x, ball_y
    while x < NB_LINE -1:
        for ball in balls:
            if (x+1, y) == ball["position"]:
                return y, x
        if tableau[y][x][2] == True:
            break
        x += 1
        print(x)
    return y, x

def move_left(ball_y, ball_x):  #inverse
    x, y = ball_x, ball_y
    while x > 0:
        for ball in balls:
            if (x-1, y) == ball["position"]:
                return y, x
        if tableau[y][x][3] == True:
            break
        x -= 1
        print(x)
    return y, x

def move_up(ball_y, ball_x):  #inverse
    x, y = ball_x, ball_y
    while y > 0:
        for ball in balls:
            if (x, y-1) == ball["position"]:
                return y, x
        if tableau[y][x][0] == True:
            break
        y -= 1
        print(y)
    return y, x

def move_down(ball_y, ball_x): #inverse
    x, y = ball_x, ball_y
    while y < NB_LINE-1:
        for ball in balls:
            if (x, y+1) == ball["position"]:
                return y, x
        if tableau[y][x][1] == True:
            break
        y += 1
        print(y)
    return y, x

def win(selected_ball, nx, ny):
    global message_victoire
    global message_result
    print("WIN")
    print(selected_ball["color"])
    print(selected_ball["position"])
    print(goal_act)
    if selected_ball["color"] != goal_act[2][0]:
        print("color check Flase")
        canvas.delete(message_victoire)
        canvas.delete(message_result)
        return False
    if (nx, ny) != (goal_act[0], goal_act[1]):
        print("pos check False")
        canvas.delete(message_victoire)
        return False
    print(compteur)
    return True

def move_ball(selected_ball, symbole): #inverse
    global balls
    global compteur
    global message_victoire
    global message_result

    compteur += 1
    
    x,y = selected_ball["position"]
    # On definit la direction
    if symbole == "Right":
        ny, nx = move_right(y, x)
    elif symbole == "Left":
        ny, nx = move_left(y, x)
    elif symbole == "Up":
        ny, nx = move_up(y, x)
    elif symbole == "Down":
        ny, nx = move_down(y, x)
    # Deplace en fonction de la direction
    print("new x: {0}, new y: {1}".format(x, y))
    selected_ball_index = balls.index(selected_ball)
    #print("selected_ball_index = ", selected_ball_index)
    #print("balls[selected_ball_index] = ", balls[selected_ball_index])
    balls[selected_ball_index]["position"] = (nx, ny)
    #print("balls[selected_ball_index] = ", balls[selected_ball_index])
    erase_balls(tableau, x, y)
    show_balls(tableau, balls)
    
    if win(selected_ball, nx, ny):
        #fonction qui affiche la victoire
        message_victoire = canvas.create_text(1200, 200, text="BRAVO VOUS AVEZ GAGNE !!")
        message_result = canvas.create_text(1150, 180 ,text = compteur, font='Arial 16 italic', fill = 'blue')
        print(compteur)
        reset(tableau, True)
        return 


# Gestion des mouvements
def handle_keypress(event):
    global selected_ball
    global fleche_liste
    print("handle_keypress: ", selected_ball)
    print(event, selected_ball)
    if selected_ball != None:
        print("when keypress:", selected_ball)
        move_ball(selected_ball, event.keysym)
        fleche_liste.append([event.keysym, selected_ball["color"]])
        show_arrow()


# Selection d'une balle
def get_clicked_ball(event_x, event_y): #inverse
    for ball in balls:
        ball_x, ball_y = ball["position"]
        ball_x0, ball_y0 = ball_x * cote, ball_y * cote
        ball_x1, ball_y1 = cote * (ball_x + 1), cote * (ball_y + 1)
        if (event_x > ball_x0 and event_x < ball_x1) and (event_y > ball_y0 and event_y < ball_y1):
            print("ball choisit")
            return ball
    print("None")
    return None

def handle_reset(event_x, event_y):
    if (event_x > 6*cote and event_x < 9*cote) and (event_y > 6*cote and event_y < 9*cote):
        reset(tableau, False)

# Gestion des selections
def handle_click(event): #ok
    global selected_ball
    print(event)
    event_x, event_y = event.x, event.y
    selected_ball = get_clicked_ball(event_x, event_y)
    handle_reset(event_x, event_y)
    print(selected_ball)

# Bind une touche event pour handle_keypress()
root.bind("<Key>", handle_keypress)
root.bind("<Button-1>", handle_click)


#Historique de déplacement

canvas.create_rectangle(850, 250, 1500, 1000, width = 15, outline = "red")

fleche_img_liste = {
    "bd": PhotoImage(file='flechebleu_bas.ppm'),
    "br": PhotoImage(file='flechebleu_droite.ppm'),
    "bl": PhotoImage(file='flechebleu_gauche.ppm'),
    "bu": PhotoImage(file='flechebleu_haut.ppm'),

    "rd": PhotoImage(file='flecherouge_bas.ppm'),
    "rr": PhotoImage(file='flecherouge_droite.ppm'),
    "rl": PhotoImage(file='flecherouge_gauche.ppm'),
    "ru": PhotoImage(file='flecherouge_haut.ppm'),

    "yd": PhotoImage(file='flechejaune_bas.ppm'),
    "yr": PhotoImage(file='flechejaune_droite.ppm'),
    "yl": PhotoImage(file='flechejaune_gauche.ppm'),
    "yu": PhotoImage(file='flechejaune_haut.ppm'),
    
    "gd": PhotoImage(file='flechevert_bas.ppm'),
    "gr": PhotoImage(file='flechevert_droite.ppm'),
    "gl": PhotoImage(file='flechevert_gauche.ppm'),
    "gu": PhotoImage(file='flechevert_haut.ppm'),
}
def show_arrow():
    x = 880
    y = 290
    x_decalage = 40
    y_decalage = 60
    nb_fleche_ligne = 13
    nb_lignes = len(fleche_liste) // nb_fleche_ligne + 1
    current_row = 0
    for i, flechedata in enumerate(fleche_liste):
        fleche, color = flechedata[0], flechedata[1]
        print("color", color)
        if color == "red" and fleche == "Down" : 
            canvas.create_image(x, y, image=fleche_img_liste["rd"])
        elif color == "red" and fleche == "Up" : 
            canvas.create_image(x, y, image=fleche_img_liste["ru"])
        elif color == "red" and fleche == "Left" : 
            canvas.create_image(x, y, image=fleche_img_liste["rl"])
        elif color == "red" and fleche == "Right" : 
            canvas.create_image(x, y, image=fleche_img_liste["rr"])

        elif color == "blue" and fleche == "Down" : 
            canvas.create_image(x, y, image=fleche_img_liste["bd"])
        elif color == "blue" and fleche == "Up" : 
            canvas.create_image(x, y, image=fleche_img_liste["bu"])
        elif color == "blue" and fleche == "Left" : 
            canvas.create_image(x, y, image=fleche_img_liste["bl"])
        elif color == "blue" and fleche == "Right" : 
            canvas.create_image(x, y, image=fleche_img_liste["br"])
        
        elif color == "green" and fleche == "Down" : 
            canvas.create_image(x, y, image=fleche_img_liste["gd"])
        elif color == "green" and fleche == "Up" : 
            canvas.create_image(x, y, image=fleche_img_liste["gu"])
        elif color == "green" and fleche == "Left" : 
            canvas.create_image(x, y, image=fleche_img_liste["gl"])
        elif color == "green" and fleche == "Right" : 
            canvas.create_image(x, y, image=fleche_img_liste["gr"])
        
        elif color == "yellow" and fleche == "Down" : 
            canvas.create_image(x, y, image=fleche_img_liste["yd"])
        elif color == "yellow" and fleche == "Up" : 
            canvas.create_image(x, y, image=fleche_img_liste["yu"])
        elif color == "yellow" and fleche == "Left" : 
            canvas.create_image(x, y, image=fleche_img_liste["yl"])
        elif color == "yellow" and fleche == "Right" : 
            canvas.create_image(x, y, image=fleche_img_liste["yr"])
        x += 45
        if i % 13 == 0 and i > 0:
            current_row += 1
            x = 880
        y = 290 + 45 * current_row
        print("currenrt row", current_row)


#Logo restart
img = PhotoImage(file='restart.ppm')
canvas.create_image(352, 352, image=img)

#fonctions
tableau_coord = placer_case(tableau)
quadrillage()
creer_mur(tableau)
show_balls(tableau, balls)
pick_goal()
show_goal()

canvas.pack()
root.mainloop()
