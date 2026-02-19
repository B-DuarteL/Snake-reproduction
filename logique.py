# Directions
NORD = (0, -1)
SUD = (0, 1)
EST = (1, 0)
OUEST = (-1, 0)

def init_serpent(nombre_cases=20):
    """Initialise le serpent au centre avec 3 segments."""
    centre = nombre_cases // 2
    return [(centre, centre), (centre - 1, centre), (centre - 2, centre)]

def collision_mur(serpent, nombre_cases=20):
    """Vérifie si la tête sort de la grille 20x20."""
    return serpent[0][0] < 0 or serpent[0][0] >= nombre_cases or serpent[0][1] < 0 or serpent[0][1] >= nombre_cases

def collision_soi_meme(serpent):
    """Vérifie si la tête touche le corps."""
    tete = serpent[0]
    corps = serpent[1:]
    return tete in corps

