###################################
# Import des librairies

import tkinter as tk
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
    2048: (242, 197, 0),
    4096: (242, 197, 0),
    8192: (242, 197, 0),
    16384: (242, 197, 0),
    32768: (242, 197, 0),
    65536: (242, 197, 0),
    131072: (242, 197, 0),
}


###################################
# Variables globales

configuration_courante = [
    ["A1", 0, 0, 0], ["A2", 0, 0, 0], ["A3", 0, 0, 0], ["A4", 0, 0, 0],
    ["B1", 0, 0, 0], ["B2", 0, 0, 0], ["B3", 0, 0, 0], ["B4", 0, 0, 0],
    ["C1", 0, 0, 0], ["C2", 0, 0, 0], ["C3", 0, 0, 0], ["C4", 0, 0, 0],
    ["D1", 0, 0, 0], ["D2", 0, 0, 0], ["D3", 0, 0, 0], ["D4", 0, 0, 0]
]

score = 0


###################################
# Définition des fonctions

def print_configuration_courante():
    """Affiche dans le terminale la configuration courante proprement."""
    print()
    print(configuration_courante[0][1], configuration_courante[1][1], configuration_courante[2][1], configuration_courante[3][1])
    print(configuration_courante[4][1], configuration_courante[5][1], configuration_courante[6][1], configuration_courante[7][1])
    print(configuration_courante[8][1], configuration_courante[9][1], configuration_courante[10][1], configuration_courante[11][1])
    print(configuration_courante[12][1], configuration_courante[13][1], configuration_courante[14][1], configuration_courante[15][1])


def rgb_hack(rgb):
    """Fonction qui permet de travailler avec des couleurs RGB (https://pythonguides.com/python-tkinter-colors/)."""
    return "#%02x%02x%02x" % rgb


def spawner_tuile_aleatoire():
    """Fait apparaître une tuile aléatoire de valeur 2 ou 4 (lancée après chaque déplacement)."""
    cases_libres = []
    for j in configuration_courante:
        if j[1] == 0:
            cases_libres.append(j)
    case_choisie = rd.choice(cases_libres)
    case_choisie[1] = rd.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])
    affichage_configuration_courante()


def exterminatus():
    """Corrige les erreurs d'affichage en cherchant et supprimant les objets du canevas qui n'ont pas d'équivalent dans la configuration courante."""
    tmp = canevas.find_all()
    for x in tmp:
        if any(x in i for i in configuration_courante):
            pass
        elif any(x not in i for i in configuration_courante) and x not in [1, 2, 3, 4, 5, 6]:
            canevas.delete(x)


victoire_var = 0
def victoire():
    """Vérifie si les conditions de victoire sont présentes et le cas échéant affiche la fin du jeu (issue : victoire)."""
    tmp = [i[1] for i in configuration_courante]
    if 2048 in tmp:
        label_victoire.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        bouton_continuer.place(relx=0.2375, rely=0.58, anchor=tk.CENTER)
        bouton_recommencer.place(relx=0.3625, rely=0.58, anchor=tk.CENTER)


def declarer_forfait():
    """Déclenchée manuellement, affiche la fin du jeu (issue : défaite)."""
    label_defaite.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    bouton_recommencer.place(relx=0.2375, rely=0.58, anchor=tk.CENTER)
    bouton_quitter.place(relx=0.3625, rely=0.58, anchor=tk.CENTER)


def recommencer():
    """Supprime les labels et boutons liés aux fin de jeu, remet le score à 0, réinitialise la configuration courante et supprime toutes les tuiles."""
    global score
    score = 0
    tmp = canevas.find_all()
    for x in tmp[6:]:
        canevas.delete(x)
    for i in configuration_courante:
        i[1], i[2], i[3] = 0, 0, 0
    score = 0
    label_victoire.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_continuer.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    label_defaite.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_recommencer.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_quitter.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    affichage_configuration_courante()
    spawner_tuile_aleatoire()
    spawner_tuile_aleatoire()


def continuer():
    """Supprime les labels et boutons liés aux fin de jeu pour permettre au joueur de continuer à jouer après la victoire (2048)."""
    global victoire_var
    label_victoire.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_continuer.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_recommencer.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    label_defaite.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    bouton_quitter.place(relx=1.5, rely=1.5, anchor=tk.CENTER)
    victoire_var = 1


def affichage_configuration_courante():
    """Met à jour la grille affichée en consultant la configuration courante.
       Appelée à chaque fin de déplacement."""
    for i in configuration_courante: # passe en revue toutes les tuiles de la config courante
        if i[1] != 0: # vérifie que la valeur de la tuile consultée est non nulle (si nulle, rien à afficher)
            i[2] = canevas.create_rectangle(position[i[0]], fill=rgb_hack(couleurs[i[1]]))
            # ajoute à la config courante un objet rectangle et l'affiche sur la grille
            i[3] = canevas.create_text(position[i[0]][0]+125//2, position[i[0]][3]-125//2, text=i[1], fill="black", font=('Helvetica','30'))
            # ajoute un text avec la valeur de la tuile à la config courante et l'affiche sur la grille
    exterminatus()
    affichage_score()
    if victoire_var == 0:
        victoire()


playable = 0
def play():
    """Ne peut être lancée qu'une fois, fait apparaître deux tuiles aléatoires."""
    global playable
    if playable == 0:
        spawner_tuile_aleatoire()
        spawner_tuile_aleatoire()
    playable = 1


def play_clavier(event):
    """Similaire à play() mais utilisée par le raccourcis clavier."""
    play()


def destroy_clavier(event):
    """Détruit (ferme) la fenêter, utilisée par le clavier."""
    racine.destroy()


def declarer_forfait_clavier(event):
    """Similaire à declarer_forfait() mais utilisée par le raccourcis clavier."""
    declarer_forfait()


def affichage_score():
    """Affiche et tient à jour le score."""
    global score
    label_score.config(text=("score : " + str(score)))

score_sauvegarde = 0
def save_config():
    global score_sauvegarde
    score_sauvegarde = score
    tmp = []
    for i in configuration_courante:
        tmp.append(i[1])
    fic = open("sauvegarde.txt", "w")
    for i in tmp:
        fic.write(str(i) + " ")
    fic.close()


def load_config ():
    global score
    score = score_sauvegarde
    fic = open("sauvegarde.txt", "r")
    tmp2 = canevas.find_all()
    for x in tmp2[6:]:
        canevas.delete(x)
    for i in configuration_courante:
        i[1], i[2], i[3] = 0, 0, 0
    while True:
        ligne = fic.readline()
        if ligne == "":
            break
        tmp = ligne.split()
    for i, j in zip(tmp, range(len(tmp))):
        configuration_courante[j][1] = int(i)
    affichage_configuration_courante()



def deplacer_haut():
    """Déplace toutes les tuiles vers le haut si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    global score
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
                score += configuration_courante[j-4][1]
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


def deplacer_haut_clavier(event):
    """Similaire à deplacer_haut mais utilisée par le raccourcis clavier."""
    deplacer_haut()


def deplacer_bas():
    """Déplace toutes les tuiles vers le bas si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    global score
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
                score += configuration_courante[j+4][1]
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


def deplacer_bas_clavier(event):
    """Similaire à deplacer_bas mais utilisée par le raccourcis clavier."""
    deplacer_bas()


def deplacer_gauche():
    """Déplace toutes les tuiles vers la gauche si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    global score
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
                score += configuration_courante[j-1][1]
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()
    

def deplacer_gauche_clavier(event):
    """Similaire à deplacer_gauche mais utilisée par le raccourcis clavier."""
    deplacer_gauche()


def deplacer_droite():
    """Déplace toutes les tuiles vers la droite si possible (en fonction de si la place est libre ou de si il faut fusionner)."""
    global score
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
                score += configuration_courante[j+1][1]
    affichage_configuration_courante()
    if tmp == 1:
        spawner_tuile_aleatoire()


def deplacer_droite_clavier(event):
    """Similaire à deplacer_droite mais utilisée par le raccourcis clavier."""
    deplacer_droite()


###################################
# Programme principal

## définitions des widgets
racine = tk.Tk()
racine.configure(bg=rgb_hack((30, 30, 30)))
racine.title('2048')
racine.geometry('1000x600+200+100')
racine.resizable(False, False)

canevas = tk.Canvas(racine, bg=rgb_hack((53, 53, 53)),bd=0, highlightthickness=2, \
                    highlightbackground=rgb_hack((0, 0, 0)), height=500, width=500)

bouton_haut = tk.Button(racine, text="↑", command=deplacer_haut, font=('Helvetica','15'))
bouton_bas = tk.Button(racine, text="↓", command=deplacer_bas, font=('Helvetica','15'))
bouton_gauche = tk.Button(racine, text="←", command=deplacer_gauche, font=('Helvetica','15'))
bouton_droite = tk.Button(racine, text="→", command=deplacer_droite, font=('Helvetica','15'))

bouton_play = tk.Button(racine, text="Play", command=play, font=('Helvetica','15'))
bouton_exit = tk.Button(racine, text="Exit", command=racine.destroy, font=('Helvetica','15'))
bouton_save = tk.Button(racine, text="Save", font=('Helvetica','15'))
bouton_load = tk.Button(racine, text="Load", font=('Helvetica','15'))

bouton_spawn = tk.Button(racine, text="spawn", command=spawner_tuile_aleatoire)
bouton_config = tk.Button(racine, text="config", command=affichage_configuration_courante)

label_score = tk.Label(racine, text="score : 0", font=('Helvetica','15'))

label_victoire = tk.Label(racine, text=("Victoire ! Vous avez atteint la tuile 2048.\n Votre score final est " + str(score) + ".\n" + "Souhaitez-vous continuer à jouer ?"), font=('Helvetica','15'))
bouton_continuer = tk.Button(racine, text=("Continuer"), font=('Helvetica','15'), command=continuer)
bouton_recommencer = tk.Button(racine, text=("Recommencer"), font=('Helvetica','15'), command=recommencer)

label_defaite = tk.Label(racine, text=("Défaite ! Vous avez déclaré forfait.\n Votre score final est " + str(score) + ".\n" + "Souhaitez-vous recommencer ?"), font=('Helvetica','15'))
bouton_quitter = tk.Button(racine, text=("Quitter"), font=('Helvetica','15'), command=racine.destroy)
bouton_declarer_forfait = tk.Button(racine, text="Déclarer forfait", font=('Helvetica','15'), command=declarer_forfait)

bouton_sauver = tk.Button(racine, text="Sauver", font=('Helvetica','15'), command=save_config)
bouton_charger = tk.Button(racine, text="Charger", font=('Helvetica','15'), command=load_config)

## placement des widgets
canevas.place(x=50, y=50)
for x in range(3): # création des lignes
    canevas.create_line(125*(x+1), 0, 125*(x+1), 502, fill=rgb_hack((0, 0, 0)), width=2)
for y in range(3): # idem
    canevas.create_line(0, 125*(y+1), 502, 125*(y+1), fill=rgb_hack((0, 0, 0)), width=2)
bouton_haut.place(relx=0.775, rely=0.45, anchor=tk.CENTER)
bouton_bas.place(relx=0.775, rely=0.55, anchor=tk.CENTER)
bouton_gauche.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
bouton_droite.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

bouton_play.place(relx=0.7, rely=0.604, anchor=tk.CENTER)
bouton_exit.place(relx=0.75, rely=0.604, anchor=tk.CENTER)
bouton_save.place(relx=0.8, rely=0.604, anchor=tk.CENTER)
bouton_load.place(relx=0.85, rely=0.604, anchor=tk.CENTER)

label_score.place(relx=0.3, rely=0.04, anchor=tk.CENTER)

bouton_declarer_forfait.place(relx=0.775, rely=0.708, anchor=tk.CENTER)
bouton_sauver.place(relx=0.7, rely=0.8125, anchor=tk.CENTER)
bouton_charger.place(relx=0.85, rely=0.8125, anchor=tk.CENTER)

racine.bind('<z>', deplacer_haut_clavier)
racine.bind('<s>', deplacer_bas_clavier)
racine.bind('<q>', deplacer_gauche_clavier)
racine.bind('<d>', deplacer_droite_clavier)

racine.bind('<Up>', deplacer_haut_clavier)
racine.bind('<Down>', deplacer_bas_clavier)
racine.bind('<Left>', deplacer_gauche_clavier)
racine.bind('<Right>', deplacer_droite_clavier)

racine.bind('<p>', play_clavier)
racine.bind('<Escape>', destroy_clavier)
racine.bind('<f>', declarer_forfait_clavier)

## boucle principale
affichage_configuration_courante()
tk.mainloop()
