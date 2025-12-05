import random
# Di re ct io ns : ( dx , dy )
NORD = (0 , -1)
SUD = (0 , 1)
EST = (1 , 0)
OUEST = ( -1 , 0)
def i n i t _ s e r p e n t () :
" " " In it ia li se le serpent au centre ( longueur 3) .
" " "
centre = 10 # Pour une grille 20 x20
return [( centre , centre ) , ( centre -1 , centre ) , ( centre -2 , centre ) ]
