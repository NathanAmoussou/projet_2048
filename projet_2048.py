###################################
# Import des librairies

import tkinter as tk


###################################
# Constantes




###################################
# Variables globales




###################################
# Définition des fonctions

def rgb_hack(rgb):
    """Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/)."""
    return "#%02x%02x%02x" % rgb



###################################
# Programme principal

# définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')
canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)), highlightthickness=1, highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

# placement des widgets
canevas.place(x=50, y=50)

# boucle principale
tk.mainloop()
