import random
import tkinter as tk
root = tk.Tk()
racine = tk.Tk()

#CREATION CANVAS
 
HAUTEUR = 780
LARGEUR = 780
cote = 48.75
 
NB_COL =16
NB_LINE = 16

canvas = tk.Canvas(bg = "white", width = LARGEUR, height = HAUTEUR)


tableau = [[[True,False,False,True],[True,False,True,False],[True,False,False,True],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,True],[True,False,False,False],[True,False,False,False],[True,True,False,False],[True,False,False,False],[True,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,True],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,True,True],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False]],
			[[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False]],
			[[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,True,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[True,False,True,False],[False,False,False,True],[False,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,True,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,True,False],[False,True,False,True],[False,False,False,False],[False,True,True,False]],
			[[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[True,False,True,False],[False,False,False,False],[False,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False],[True,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,True,True,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,False,False,True],[False,False,False,False],[False,True,True,False],[False,False,False,True],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,True,False]],
			[[False,True,False,True],[False,True,False,False],[True,True,False,False],[False,True,True,False],[False,True,False,True],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,True,False],[False,True,False,True],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,False,False],[False,True,True,False]]]

def coord_carre(i,j):
    x0,y0= cote*j, cote*i
    x1,y1= cote*(j+1), cote*(i+1)
    return [[x0,y0],[x1,y1]]

def quadrillage():
    y = 0
    while y <=780 :
        canvas.create_line(0,y,HAUTEUR,y, fill = "black")
        y += cote
 
    x = 0
    while x <=780 :
        canvas.create_line(x,0,x,LARGEUR, fill = "black")
        x += cote

def placer_case(tableau):
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            tableau[i][j].append(coord_carre(i,j))
    return tableau

def creer_mur(tableau):
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

def redemarrer():
    pass
 
def sauvegarde():
    pass
 
def ecraser_sauv():
    pass

#CREATION BOUTON REDEMARRER
bouton = tk.Button(racine, text = "redemarrer", command = redemarrer)
bouton.grid(row = 1)
 
#CREATION BOUTON SAUVEGARDE
bouton = tk.Button(racine, text = "sauvegarde", command = sauvegarde)
bouton.grid(row = 2)
#CREATION BOUTON EFFACER
bouton = tk.Button(racine, text = "ecraser la sauvegarde", command = ecraser_sauv)
bouton.grid(row = 3)
#CREATION FENETRE HISTORIQUE
 
canvas.create_rectangle(850, 250, 1470, 600, width = 15)

"""tableau = create_tableau(3,3)"""
tableau_coord = placer_case(tableau)

 
quadrillage()
creer_mur(tableau)
canvas.pack()
root.mainloop()

creer_mur(tableau)
canvas.pack()   
root.mainloop()

# Entrée on a un tableau  carré avec n ligne et n colonne
# Chaque case est un quadruplée qui contient potentiellement des murs

#créer la carte à la main [[False, True,False,False]]...

#Créer une fonction qui gère les déplacements
#créer un 'pion' qui va se déplacer
#Afficher le pion sur la bonne case

