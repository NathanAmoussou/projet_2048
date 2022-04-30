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
    ["D1", 2, 0, 0], ["D2", 0, 0, 0], ["D3", 4, 0, 0], ["D4", 0, 0, 0]
]


###################################
# Définition des fonctions

def rgb_hack(rgb):
    """Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/)."""
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
        elif j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == configuration_courante[j][1]:
            configuration_courante[j-4][1] += configuration_courante[j][1]
            configuration_courante[j][1] = 0
        print(i, j)


def deplacer_haut_x4():
    for i in range(3):
        deplacer_haut()


def deplacer_bas():
    for i, j in zip(configuration_courante, range(len(configuration_courante))):
        print(i, j)
        if j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == 0:
            configuration_courante[j][1], configuration_courante[j+4][1] = 0, i[1]
            canevas.delete(i[2])
            canevas.delete(i[3])
        elif j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == configuration_courante[j][1]:
            configuration_courante[j+4][1] += configuration_courante[j][1]
            configuration_courante[j][1] = 0


def deplacer_bas_x4():
    for i in range(3):
        deplacer_bas()


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
deplacer_bas_x4()
affichage_configuration_courante()

tk.mainloop()
