###################################
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
    """Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/)."""
    return "#%02x%02x%02x" % rgb


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
tk.mainloop()
