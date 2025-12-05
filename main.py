import random
import tkinter as tk
# Di re ct io ns : ( dx , dy )
NORD = (0 , -1)
SUD = (0 , 1)
EST = (1 , 0)
OUEST = ( -1 , 0)
def init_serpent() :
    """ Initialise le serpent au centre ( longueur 3) ."""
    centre = 10 # Pour une grille 20 x20
    return [( centre , centre ) , ( centre -1 , centre ) , ( centre -2 , centre ) ]
# 1. Creation de la fenetre principale (Root)
fenetre = tk.Tk()
fenetre.title("SNAKE")
fenetre.geometry("800x600")