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

# définitions des widgets
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

tuile_test = canevas.create_rectangle(125, 125, 250, 250, fill=rgb_hack((0, 0, 0)))


# placement des widgets
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

# boucle principale
tk.mainloop()
