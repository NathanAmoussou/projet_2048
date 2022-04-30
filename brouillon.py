# version un avec la tuile noir
"""###################################
# Import des librairies

import tkinter as tk
from turtle import bgcolor


###################################
# Constantes

LARGEUR_TUILE = 125
LONGUEUR_TUILE = 125


###################################
# Variables globales




###################################
# Définition des fonctions

def rgb_hack(rgb):
    # Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/).
    return "#%02x%02x%02x" % rgb


def deplacement_right_test():
    global test_x
    if test_x < 375:
        canevas.move(tuile_test, 125, 0)
        test_x += 125
def deplacement_left_test():
    global test_x
    if test_x > 0:
        canevas.move(tuile_test, -125, 0)
        test_x += -125
def deplacement_up_test():
    global test_y
    if test_y > 125:
        canevas.move(tuile_test, 0, -125)
        test_y += -125
def deplacement_down_test():
    global test_y
    if test_y < 500:
        canevas.move(tuile_test, 0, 125)
        test_y += 125


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_left = tk.Button(racine, text='Left', bg=rgb_hack((37, 37, 37)), command=deplacement_left_test)
bouton_right = tk.Button(racine, text='Right', bg=rgb_hack((37, 37, 37)), command=deplacement_right_test)
bouton_up = tk.Button(racine, text='Up', bg=rgb_hack((37, 37, 37)), command=deplacement_up_test)
bouton_down = tk.Button(racine, text='Down', bg=rgb_hack((37, 37, 37)), command=deplacement_down_test)

tuile_test = canevas.create_rectangle(125, 125, 250, 250, fill=rgb_hack((238, 228, 218)))

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
bouton_left.place(x=700, y=300) # boutons très moches juste pour tester
bouton_right.place(x=700, y=350) # boutons très moches juste pour tester
bouton_up.place(x=700, y=325) # boutons très moches juste pour tester
bouton_down.place(x=700, y=375) # boutons très moches juste pour tester

test_c = canevas.coords(tuile_test) # temporaire, c'est juste pour les tests
test_x = test_c[1]
test_y = test_c[2]

## boucle principale
tk.mainloop()
"""

# version 2 avec la tuile blanche qui se déplace et collision
"""# Import des librairies

import tkinter as tk
from turtle import bgcolor


###################################
# Constantes

LARGEUR_TUILE = 125
LONGUEUR_TUILE = 125


###################################
# Variables globales




###################################
# Définition des fonctions

def rgb_hack(rgb):
    # Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/).
    return "#%02x%02x%02x" % rgb


def deplacement_right_test():
    global test_x
    if test_x < 375:
        canevas.move(tuile_test, 125, 0)
        test_x += 125
def deplacement_left_test():
    global test_x
    if test_x > 0:
        canevas.move(tuile_test, -125, 0)
        test_x += -125
def deplacement_up_test():
    global test_y
    if test_y > 125:
        canevas.move(tuile_test, 0, -125)
        test_y += -125
def deplacement_down_test():
    global test_y
    if test_y < 500:
        canevas.move(tuile_test, 0, 125)
        test_y += 125


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_left = tk.Button(racine, text='Left', bg=rgb_hack((37, 37, 37)), command=deplacement_left_test)
bouton_right = tk.Button(racine, text='Right', bg=rgb_hack((37, 37, 37)), command=deplacement_right_test)
bouton_up = tk.Button(racine, text='Up', bg=rgb_hack((37, 37, 37)), command=deplacement_up_test)
bouton_down = tk.Button(racine, text='Down', bg=rgb_hack((37, 37, 37)), command=deplacement_down_test)

tuile_test = canevas.create_rectangle(125, 125, 250, 250, fill=rgb_hack((238, 228, 218)))

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
bouton_left.place(x=700, y=300) # boutons très moches juste pour tester
bouton_right.place(x=700, y=350) # boutons très moches juste pour tester
bouton_up.place(x=700, y=325) # boutons très moches juste pour tester
bouton_down.place(x=700, y=375) # boutons très moches juste pour tester

test_c = canevas.coords(tuile_test) # temporaire, c'est juste pour les tests
test_x = test_c[1]
test_y = test_c[2]

## boucle principale
tk.mainloop()"""

# version 3 avec la tuile blanche et le label qui suit
"""
# Import des librairies

import tkinter as tk
from turtle import bgcolor


###################################
# Constantes

LARGEUR_TUILE = 125
LONGUEUR_TUILE = 125


###################################
# Variables globales




###################################
# Définition des fonctions

def rgb_hack(rgb):
    # Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/).
    return "#%02x%02x%02x" % rgb


def deplacement_right_test():
    global test_x
    if test_x < 375:
        canevas.move(tuile_test, 125, 0)
        test_x += 125
        canevas.move(tuile_test_text, 125, 0)
def deplacement_left_test():
    global test_x
    if test_x > 0:
        canevas.move(tuile_test, -125, 0)
        test_x += -125
        canevas.move(tuile_test_text, -125, 0)
def deplacement_up_test():
    global test_y
    if test_y > 125:
        canevas.move(tuile_test, 0, -125)
        test_y += -125
        canevas.move(tuile_test_text, 0, -125)
def deplacement_down_test():
    global test_y
    if test_y < 500:
        canevas.move(tuile_test, 0, 125)
        test_y += 125
        canevas.move(tuile_test_text, 0, 125)


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_left = tk.Button(racine, text='Left', bg=rgb_hack((37, 37, 37)), command=deplacement_left_test)
bouton_right = tk.Button(racine, text='Right', bg=rgb_hack((37, 37, 37)), command=deplacement_right_test)
bouton_up = tk.Button(racine, text='Up', bg=rgb_hack((37, 37, 37)), command=deplacement_up_test)
bouton_down = tk.Button(racine, text='Down', bg=rgb_hack((37, 37, 37)), command=deplacement_down_test)

tuile_test = canevas.create_rectangle(125, 125, 250, 250, fill=rgb_hack((238, 228, 218)))

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
bouton_left.place(x=700, y=300) # boutons très moches juste pour tester
bouton_right.place(x=700, y=350) # boutons très moches juste pour tester
bouton_up.place(x=700, y=325) # boutons très moches juste pour tester
bouton_down.place(x=700, y=375) # boutons très moches juste pour tester

test_c = canevas.coords(tuile_test) # temporaire, c'est juste pour les tests
test_x = test_c[1]
test_y = test_c[2]

tuile_test_text = canevas.create_text(test_x+125//2, test_y-125//2, text="2", fill="black")
print(test_c)

## boucle principale
tk.mainloop()"""

"""position = {
    "A1": [0, 0], "A2": [0, 125], "A3": [0, 250], "A4": [0, 375],
    "B1": [125, 0], "B2": [125, 125], "B3": [125, 250], "B4": [125, 375],
    "C1": [250, 0], "C2": [250, 125], "C3": [250, 250], "C4": [250, 375],
    "D1": [375, 0], "D2": [375, 125], "D3": [375, 250], "D4": [375, 375]
}"""

"""tuile_1 = canevas.create_rectangle(position2["B1"], fill=rgb_hack((238, 228, 218)))
valeur_1 = canevas.create_text(canevas.coords(tuile_1)[0]+125//2, canevas.coords(tuile_1)[3]-125//2, text="2", fill="black")

tuile_2 = canevas.create_rectangle(position2["A3"], fill=rgb_hack((238, 228, 218)))
valeur_2 = canevas.create_text(canevas.coords(tuile_2)[0]+125//2, canevas.coords(tuile_2)[3]-125//2, text="4", fill="black")

tuile_3 = canevas.create_rectangle(position2["C4"], fill=rgb_hack((238, 228, 218)))
valeur_3 = canevas.create_text(canevas.coords(tuile_3)[0]+125//2, canevas.coords(tuile_3)[3]-125//2, text="4", fill="black")"""

"""for x in range(4):
    configuration_de_depart.append(rd.choice(list(position2.keys())))
print(configuration_de_depart)"""

"""def affichage_configuration_courante():
    for i in configuration_courante:
        if i[1] != 0:
            canevas.create_rectangle(position[i[0]], fill=rgb_hack((238, 228, 218)))
            canevas.create_text(position[i[0]][0]+125//2, position[i[0]][3]-125//2, text=i[1], fill="black")"""

"""
###################################
# Import des librairies

import tkinter as tk
from turtle import bgcolor
import random as rd


###################################
# Constantes

LARGEUR_TUILE = 125
LONGUEUR_TUILE = 125

position = {
    "A1": [0, 0, 125, 125], "A2": [125, 0, 250, 125], "A3": [250, 0, 375, 125], "A4": [375, 0, 500, 125],
    "B1": [0, 125, 125, 250], "B2": [125, 125, 250, 250], "B3": [250, 125, 375, 250], "B4": [375, 125, 500, 250],
    "C1": [0, 250, 125, 375], "C2": [125, 250, 250, 375], "C3": [250, 250, 375, 375], "C4": [375, 250, 500, 375],
    "D1": [0, 375, 125, 500], "D2": [125, 375, 250, 500], "D3": [250, 375, 375, 500], "D4": [375, 375, 500, 500]
}


###################################
# Variables globales

configuration_courante = [
    ["A1", 2, 0, 0], ["A2", 0, 0, 0], ["A3", 0, 0, 0], ["A4", 0, 0, 0],
    ["B1", 0, 0, 0], ["B2", 2, 0, 0], ["B3", 0, 0, 0], ["B4", 0, 0, 0],
    ["C1", 2, 0, 0], ["C2", 0, 0, 0], ["C3", 0, 0, 0], ["C4", 2, 0, 0],
    ["D1", 0, 0, 0], ["D2", 0, 0, 0], ["D3", 4, 0, 0], ["D4", 0, 0, 0]
]


###################################
# Définition des fonctions

def rgb_hack(rgb):
    #Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/).
    return "#%02x%02x%02x" % rgb


def affichage_configuration_courante():
    for i in configuration_courante:
        if i[1] != 0:
            i[2] = canevas.create_rectangle(position[i[0]], fill=rgb_hack((238, 228, 218)))
            i[3] = canevas.create_text(position[i[0]][0]+125//2, position[i[0]][3]-125//2, text=i[1], fill="black")


def deplacer_haut():
    for i, j in zip(configuration_courante, range(len(configuration_courante))):
        print(i, j)
        if j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == 0:
            configuration_courante[j][1], configuration_courante[j-4][1] = 0, i[1]
            canevas.delete(i[2])
            canevas.delete(i[3])


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)


## boucle principale
affichage_configuration_courante()
deplacer_haut()
deplacer_haut()
deplacer_haut()
affichage_configuration_courante()
tk.mainloop()
"""