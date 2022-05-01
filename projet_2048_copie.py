# objectif pour 31 avril : assigner les fonctions de deplacement à des boutons et à des touches du clavier
# faire apparaitre une tuile aléatoire à chaque déplacement
# créer l'évènement victoire et défaite (si 2048 ou si plus aucun déplacement possible)


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
} # référence des coordonnées possible pour les tuiles

position2 = [
    ["A1", [0, 0]], ["A2", [125, 0]], ["A3", [250, 0]], ["A4", [375, 0]],
    ["B1", [0, 125]], ["B2", [125, 125]], ["B3", [250, 125]], ["B4", [375, 125]],
    ["C1", [0, 250]], ["C2", [125, 250]], ["C3", [250, 250]], ["C4", [375, 250]],
    ["D1", [0, 375]], ["D2", [125, 250]], ["D3", [250, 375]], ["D4", [375, 375]]
]

###################################
# Variables globales

configuration_courante = [
    ["A1", 2, 0, 0], ["A2", 0, 0, 0], ["A3", 0, 0, 0], ["A4", 0, 0, 0],
    ["B1", 0, 0, 0], ["B2", 0, 0, 0], ["B3", 0, 0, 0], ["B4", 0, 0, 0],
    ["C1", 0, 0, 0], ["C2", 0, 0, 0], ["C3", 0, 0, 0], ["C4", 0, 0, 0],
    ["D1", 0, 0, 0], ["D2", 0, 0, 0], ["D3", 0, 0, 0], ["D4", 0, 0, 0]
] # liste qui contient en permanence la configuration de la grille
# un élément de cette config prend la forme suivante ["coordonnées", valeur de tuile, rectangle de canevas, text de canevas]


###################################
# Définition des fonctions

def print_configuration_courante():
    print()
    print(configuration_courante[0], configuration_courante[1], configuration_courante[2], configuration_courante[3])
    print(configuration_courante[4], configuration_courante[5], configuration_courante[6], configuration_courante[7])
    print(configuration_courante[8], configuration_courante[9], configuration_courante[10], configuration_courante[11])
    print(configuration_courante[12], configuration_courante[13], configuration_courante[14], configuration_courante[15])



def rgb_hack(rgb):
    """Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/)."""
    return "#%02x%02x%02x" % rgb


def affichage_configuration_courante():
    """Met à jour la grille affichée en consultant la configuration courante.
       Appelée à chaque fin de déplacement."""
    for i in configuration_courante: # passe en revue toutes les tuiles de la config courante
        if i[1] != 0: # vérifie que la valeur de la tuile consultée est non nulle (si nulle, rien à afficher)
            i[2] = canevas.create_rectangle(position[i[0]], fill=rgb_hack((238, 228, 218)))
            # ajoute à la config courante un objet rectangle et l'affiche sur la grille
            i[3] = canevas.create_text(position[i[0]][0]+125//2, position[i[0]][3]-125//2, text=i[1], fill="black")
            # ajoute un text avec la valeur de la tuile à la config courante et l'affiche sur la grille


def deplacer_haut():
    """Déplace toutes les tuiles vers le haut si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == 0: # si la tuile n'est pas au bord et si la case cible est libre
                configuration_courante[j][1], configuration_courante[j-4][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()
            elif j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == configuration_courante[j][1]: # si la tuile n'est pas au bord et si la case cible est occupé de valeur égale
                configuration_courante[j-4][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()


def deplacer_bas():
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == 0:
                configuration_courante[j][1], configuration_courante[j+4][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()
            elif j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == configuration_courante[j][1]:
                configuration_courante[j+4][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()


def deplacer_gauche():
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            print(i, j)
            if (j != 0 and j != 4 and j != 8 and j != 12) and i[1] != 0 and configuration_courante[j-1][1] == 0:
                configuration_courante[j][1], configuration_courante[j-1][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()
            elif (j != 0 and j != 4 and j != 8 and j != 12) and i[1] != 0 and configuration_courante[j-1][1] == configuration_courante[j][1]:
                configuration_courante[j-1][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()


def deplacer_droite():
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            print(i, j)
            if (j != 3 and j != 7 and j != 11 and j != 15) and i[1] != 0 and configuration_courante[j+1][1] == 0:
                configuration_courante[j][1], configuration_courante[j+1][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()
            elif (j != 3 and j != 7 and j != 11 and j != 15) and i[1] != 0 and configuration_courante[j+1][1] == configuration_courante[j][1]:
                configuration_courante[j+1][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                affichage_configuration_courante()


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_haut = tk.Button(racine, text="haut", command=deplacer_haut)
bouton_bas = tk.Button(racine, text="bas", command=deplacer_bas)
bouton_gauche = tk.Button(racine, text="gauche", command=deplacer_gauche)
bouton_droite = tk.Button(racine, text="droite", command=deplacer_droite)

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
bouton_haut.place(x=750, y=250)
bouton_bas.place(x=750, y=350)
bouton_gauche.place(x=700, y=300)
bouton_droite.place(x=800, y=300)

## boucle principale
affichage_configuration_courante()
tk.mainloop()
