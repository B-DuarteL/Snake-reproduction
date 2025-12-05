import random
import tkinter as tk
import time
from logique import *
# Directions : ( dx , dy )
NORD = (0 , -1)
SUD = (0 , 1)
EST = (1 , 0)
OUEST = ( -1 , 0)
def init_serpent() :
    """ Initialise le serpent au centre ( longueur 3) ."""
    centre = 10 # Pour une grille 20 x20
    return [( centre , centre ) , ( centre -1 , centre ) , ( centre -2 , centre ) ]
# Creation de la fenetre principale (Root)


taille_case = 20  # Chaque case fait 20x20 pixels
"""nombre_cases_largeur = 20  # 20 cases en largeur
nombre_cases_hauteur = 20  # 20 cases en hauteur
largeur_canvas = nombre_cases_largeur * taille_case  # 400 pixels width 
hauteur_canvas = nombre_cases_hauteur * taille_case  # 400 pixels height 
On peut quand même utitliser cette partie si on fait un niveau avec un taille de map différente"""
nombre_cases = 20 #la grille étant un carré, il n'y a pas besoin de le faire pour chaque dimension
taille_canvas = nombre_cases * taille_case # 400 pixels width

def dessiner_grillage():
    """Dessine le grillage de 20x20"""
    # Lignes verticales
    for colonne in range(0, taille_canvas, taille_case):
        canvas.create_line(colonne, 0, colonne, taille_canvas, fill='gray20')
    
    # Lignes horizontales
    for ligne in range(0, taille_canvas, taille_case):
        canvas.create_line(0, ligne, taille_canvas, ligne, fill='gray20')

# ============ DÉMARRAGE DU JEU ============

# Créer la fenêtre
fenetre = tk.Tk()
fenetre.title("Snake")
canvas = tk.Canvas(fenetre, width=taille_canvas, height=taille_canvas, bg='black')
canvas.pack()
dessiner_grillage()
fenetre.mainloop()