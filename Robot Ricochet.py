import random
import tkinter as tk

root = tk.Tk()

""" 
affichage mal fait (14 au lieu de 15=)
done - lors de la génération des boules il ne faut pas qu'elles aillent dans le centre de la map
done - dépassement du tableau dans certains cas quand on veut déplacer les boules
done - Même quand les boules sont bien sélectionnés et update. l'info ne passe pas.
done - x, y, i, j sont inversés, il faut corrigé ça
done - les boules sont modifiés dans le backend mais le front ne s'update pas
certains murs sont traversés uniquement de bas en haut et de gauche à droite
les boules effacés le sont mal. Il faut une autre fonction
"""

#CREATION CANVAS
HAUTEUR = 780
LARGEUR = 780
cote = 44 #modif temporaire pour debug
NB_COL = 16
NB_LINE = 16
selected_ball = None
compteur = 0
goal_pos = [(1, 3), (4, 1), (5,5),(9,2),(13,1),(3,6),(4,9),(1,10),(2,14),(4,12),(6,13),(10,12),(12,13),(11,10),(13,11),(14,6),(9,2),(10,6)]
goal_act = [-1, -1, ""]
canvas = tk.Canvas(bg = "white", width = LARGEUR, height = HAUTEUR)
# colonne 10, 6/7 11/12
                                                    #0 = haut, 1 = bas, 2 = droite, 4 = gauche                                                              #0 = haut, 1 = bas, 2 = droite, 4 = gauche                      #0 = haut, 1 = bas, 2 = droite, 4 = gauche                          #0 = haut, 1 = bas, 2 = droite, 4 = gauche          #0 = haut, 1 = bas, 2 = droite, 4 = gauche                                  #0 = haut, 1 = bas, 2 = droite, 4 = gauche
#creation d'un tableau
tableau = [[[True,False,False,True],[True,False,True,False],[True,False,False,True],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,True,False],[True,False,False,True],[True,False,False,False],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,True,True],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False]],
            [[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False]],
            [[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,True,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,True,False],[False,False,False,True],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,False,False,True],[True,False,True,False],[False,False,False,True],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
            [[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,True,True,False]],
            [[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False]],
            [[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
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
        x,y = random.randint(0, NB_LINE-1), random.randint(0, NB_LINE-1)
        print("CREATED")
        while (check_ball(x, y, balls)):
            print("CHECKED")
            x,y = random.randint(0, NB_LINE-1), random.randint(0, NB_LINE-1)
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

def reset(tableau):
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
    pick_goal()
    show_goal()
    compteur = 0
    


        

"""
def create_rectangles(color_rectangle_blue):
    rectangles = []     
    n_rectangles = len(color_rectangle_blue)
    for i in range(n_rectangles):
        x,y = random.randint(0, NB_LINE-1), random.randint(0, NB_LINE-1)
        print("CREATED")
        while (check_ball(x, y, rectangles)):
            print("CHECKED")
            x,y = random.randint(0, NB_LINE-1), random.randint(0, NB_LINE-1)
        rectangles.append({
            "position": (x,y),
            "color": color_rectangle_blue [i]
        })
        print("postion = ", x, y, " color = ", color_rectangle_blue[i])
    return rectangles

rectangles = create_rectangles(color_rectangle_blue)


def show_rectangles(tableau, rectangles):
    for rectangle in rectangles :
        i,j = rectangles["position"]
        color = rectangles["color"]
        canvas.create_rectangle((i * cote)+3, (j * cote)+3, (cote * (i + 1))-3, (cote * (j + 1))-3, fill=color, outline = "white")
"""
        

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

"""
def move_to_obstacle(ball_i, ball_j, symbole, direction):
    walls_dir = {"Right": 2, "Left": 3, "Up": 0, "Down": 1}
    ball_here = False
    got_obstacle = False
    loop_i, loop_j = ball_i, ball_j
    print("Direction: ", walls_dir[symbole])
    in_table = (loop_i < NB_LINE and loop_j < NB_LINE) and (loop_i > -1 and loop_j > -1)
    while(not got_obstacle and in_table):
        in_table = (loop_i < NB_LINE and loop_j < NB_LINE) and (loop_i > 0 and loop_j > 0)
        print("loopi", loop_i, "loopj", loop_j, "in_table", in_table)
        # Test if there is a ball in the defined direction
        for ball in balls:
            if (loop_i+direction[0],loop_j+direction[1]) == ball["position"]:
                ball_here = True
                break
        if tableau[loop_i][loop_j][walls_dir[symbole]] == True or ball_here:
            got_obstacle = True
            break
        loop_i += direction[0]
        loop_j += direction[1]
    print("final loop_i", loop_i, "final loop_j", loop_j)
    return loop_i, loop_j
"""

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
    print("WIN")
    print(selected_ball["color"])
    print(selected_ball["position"])
    print(goal_act)
    if selected_ball["color"] != goal_act[2][0]:
        print("color check Flase")
        return False
    if (nx, ny) != (goal_act[0], goal_act[1]):
        print("pos check False")
        return False
    return True

def move_ball(selected_ball, symbole): #inverse
    global balls
    global compteur

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
    print("compteur = ", compteur)
    if win(selected_ball, nx, ny):
        #fonction qui affiche la victoire
        print("GG")
        print(compteur)
        reset(tableau)
        return

# Gestion des mouvements
def handle_keypress(event):
    global selected_ball
    print("handle_keypress: ", selected_ball)
    print(event, selected_ball)
    if selected_ball != None:
        print("when keypress:", selected_ball)
        move_ball(selected_ball, event.keysym)

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
        reset(tableau)

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

canvas.create_rectangle(850, 250, 1470, 600, width = 15)
tableau_coord = placer_case(tableau)
quadrillage()
creer_mur(tableau)
show_balls(tableau, balls)
pick_goal()
show_goal()
#show_rectangles(tableau, rectangles)
canvas.pack()
root.mainloop()
