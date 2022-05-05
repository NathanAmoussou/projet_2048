# objectif pour 31 avril : assigner les fonctions de deplacement à des boutons et à des touches du clavier
# faire apparaitre une tuile aléatoire à chaque déplacement
# créer l'évènement victoire et défaite (si 2048 ou si plus aucun déplacement possible)


###################################
# Import des librairies

from cgi import print_arguments
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

couleurs = {
    2: (240, 228, 217),
    4: (239, 225, 199),
    8: (253, 175, 113),
    16: (255, 143, 86),
    32: (255, 112, 82),
    64: (255, 72, 20),
    128: (240, 210, 107),
    256: (240, 207, 88),
    512: (241, 203, 65),
    1024: (242, 200, 40),
    2048: (242, 197, 0)
}


###################################
# Variables globales

configuration_courante = [
    ["A1", 0, 0, 0, "m"], ["A2", 0, 0, 0, "m"], ["A3", 2, 0, 0, "v"], ["A4", 0, 0, 0, "m"],
    ["B1", 0, 0, 0, "m"], ["B2", 0, 0, 0, "m"], ["B3", 0, 0, 0, "m"], ["B4", 0, 0, 0, "m"],
    ["C1", 0, 0, 0, "m"], ["C2", 0, 0, 0, "m"], ["C3", 0, 0, 0, "m"], ["C4", 0, 0, 0, "m"],
    ["D1", 0, 0, 0, "m"], ["D2", 0, 0, 0, "m"], ["D3", 4, 0, 0, "v"], ["D4", 2, 0, 0, "v"]
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


def spawner_tuile_aleatoire():
    cases_libres = []
    for j in configuration_courante:
        if j[1] == 0:
            cases_libres.append(j)
    case_choisie = rd.choice(cases_libres)
    case_choisie[1] = rd.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    affichage_configuration_courante()
    

def exterminatus():
    tmp = canevas.find_all()
    for x in tmp:
        if any(x in i for i in configuration_courante):
            print(x, "est dans la config courante")
        elif any(x not in i for i in configuration_courante) and x not in [1, 2, 3, 4, 5, 6]:
            #print(x, "est éliminable")
            canevas.delete(x)


def affichage_configuration_courante():
    """Met à jour la grille affichée en consultant la configuration courante.
       Appelée à chaque fin de déplacement."""
    for i in configuration_courante: # passe en revue toutes les tuiles de la config courante
        if i[1] != 0: #and i[2] == 0: # vérifie que la valeur de la tuile consultée est non nulle (si nulle, rien à afficher)
            i[2] = canevas.create_rectangle(position[i[0]], fill=rgb_hack(couleurs[i[1]]), tags="v")
            # ajoute à la config courante un objet rectangle et l'affiche sur la grille
            i[3] = canevas.create_text(position[i[0]][0]+125//2, position[i[0]][3]-125//2, text=i[1], fill="black")
            # ajoute un text avec la valeur de la tuile à la config courante et l'affiche sur la grille
    print_configuration_courante()
    print(canevas.find_all())
    exterminatus()


def play():
    spawner_tuile_aleatoire()
    spawner_tuile_aleatoire()


def deplacer_haut():
    """Déplace toutes les tuiles vers le haut si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    tmp = 0
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == 0: # si la tuile n'est pas au bord et si la case cible est libre
                configuration_courante[j][1], configuration_courante[j-4][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
            elif j-4 >= 0 and i[1] != 0 and configuration_courante[j-4][1] == configuration_courante[j][1]: # si la tuile n'est pas au bord et si la case cible est occupé de valeur égale
                configuration_courante[j-4][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


def deplacer_bas():
    tmp = 0
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == 0:
                configuration_courante[j][1], configuration_courante[j+4][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
            elif j+4 <= 15 and i[1] != 0 and configuration_courante[j+4][1] == configuration_courante[j][1]:
                configuration_courante[j+4][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


def deplacer_gauche():
    tmp = 0
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if (j != 0 and j != 4 and j != 8 and j != 12) and i[1] != 0 and configuration_courante[j-1][1] == 0:
                configuration_courante[j][1], configuration_courante[j-1][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
            elif (j != 0 and j != 4 and j != 8 and j != 12) and i[1] != 0 and configuration_courante[j-1][1] == configuration_courante[j][1]:
                configuration_courante[j-1][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()
    


def deplacer_droite():
    tmp = 0
    for i in range(3):
        for i, j in zip(configuration_courante, range(len(configuration_courante))):
            if (j != 3 and j != 7 and j != 11 and j != 15) and i[1] != 0 and configuration_courante[j+1][1] == 0:
                configuration_courante[j][1], configuration_courante[j+1][1] = 0, i[1]
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
            elif (j != 3 and j != 7 and j != 11 and j != 15) and i[1] != 0 and configuration_courante[j+1][1] == configuration_courante[j][1]:
                configuration_courante[j+1][1] += configuration_courante[j][1]
                configuration_courante[j][1] = 0
                canevas.delete(i[2])
                canevas.delete(i[3])
                i[2], i[3] = 0, 0
                tmp = 1
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_haut = tk.Button(racine, text="↑", command=deplacer_haut)
bouton_bas = tk.Button(racine, text="↓", command=deplacer_bas)
bouton_gauche = tk.Button(racine, text="←", command=deplacer_gauche)
bouton_droite = tk.Button(racine, text="→", command=deplacer_droite)

bouton_play = tk.Button(racine, text="Play", command=play)
bouton_exit = tk.Button(racine, text="Exit")
bouton_save = tk.Button(racine, text="Save")
bouton_load = tk.Button(racine, text="Load")

bouton_spawn = tk.Button(racine, text="spawn", command=spawner_tuile_aleatoire)
bouton_config = tk.Button(racine, text="config", command=affichage_configuration_courante)

#bouton_exterminatus = tk.Button(racine, text="exterminatus", command=exterminatus)

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
#bouton_haut.place(x=750, y=250)
bouton_haut.place(relx=0.775, rely=0.45, anchor=tk.CENTER)
bouton_bas.place(relx=0.775, rely=0.55, anchor=tk.CENTER)
bouton_gauche.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
bouton_droite.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

bouton_play.place(relx=0.7, rely=0.7, anchor=tk.CENTER)
bouton_exit.place(relx=0.75, rely=0.7, anchor=tk.CENTER)
bouton_save.place(relx=0.8, rely=0.7, anchor=tk.CENTER)
bouton_load.place(relx=0.85, rely=0.7, anchor=tk.CENTER)

#bouton_exterminatus.place(relx=0.775, rely=0.9, anchor=tk.CENTER)

#bouton_spawn.place(x=700, y=400)
#bouton_config.place(x=700, y =500)

## boucle principale
affichage_configuration_courante()
tk.mainloop()