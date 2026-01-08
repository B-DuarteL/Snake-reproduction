# Directions
NORD = (0, -1)
SUD = (0, 1)
EST = (1, 0)
OUEST = (-1, 0)

def init_serpent():
    """Initialise le serpent au centre avec 3 segments."""
    centre = 10
    return [(centre, centre), (centre - 1, centre), (centre - 2, centre)]

def deplacer_serpent(serpent, direction, a_mange):
    """Déplace le serpent dans la direction donnée."""
    tete_x, tete_y = serpent[0]
    dx, dy = direction
    
    nouvelle_tete = (tete_x + dx, tete_y + dy)
    
    # remplace le premier element par tete
    serpent.insert(0, nouvelle_tete)
    
    # Retirer la queue si le serpent n'a pas mangé de pomme (empeche le serpent d'etre infini)
    if not a_mange:
        serpent.pop()
    
    return serpent

def collision_mur(serpent):
    """Vérifie si la tête sort de la grille 20x20."""
    return serpent[0][0] < 0 or serpent[0][0] >= 20 or serpent[0][1] < 0 or serpent[0][1] >= 20

def collision_soi_meme(serpent):
    """Vérifie si la tête touche le corps."""
    tete = serpent[0]
    corps = serpent[1:]
    return tete in corps

