import tkinter as tk
from tkinter import messagebox
import random
from logique import *
NORD = (0, -1)
SUD = (0, 1)
EST = (1, 0)
OUEST = (-1, 0)

direction = EST
prochaine_direction = EST
pomme = None
taille_case = 20
nombre_cases = 20
taille_canvas = nombre_cases * taille_case
serpent = []
score = 0
meilleur_score = 0
jeu_en_cours = False


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

def pause():
    """Met en pause ou reprend le jeu."""
    global jeu_en_cours
    
    if jeu_en_cours:
        jeu_en_cours = False
        #change le nom du bouton quand le jeu est en pause
        bouton_pause.config(text="Reprendre")
    else:
        jeu_en_cours = True
        #change le nom du bouton quand le jeu est en cours
        bouton_pause.config(text="Mettre en Pause")
        boucle_jeu()

def placer_pomme():
    """Place une pomme à une position aléatoire (pas sur le serpent)."""
    while True:
        x = random.randint(0, nombre_cases - 1)
        y = random.randint(0, nombre_cases - 1)
        if (x, y) not in serpent:
            return (x, y)

def dessiner_grillage():
    """Dessine le grillage de 20x20"""
    for colonne in range(0, taille_canvas + 1, taille_case):# création d'une colonne qui commence à 0 avance de tout les 20 pixels jusqu'à la taille maximum du canvas
        canvas.create_line(
            colonne, 0, colonne, taille_canvas, fill='gray20'
            )
    
    for ligne in range(0, taille_canvas + 1, taille_case):# création d'une ligne qui commence à 0 avance de tout les 20 pixels jusqu'à la taille maximum du canvas
        canvas.create_line(
            0,              # x du point de départ bord gauche du canvas
            ligne,          # y du point de départ 
            taille_canvas,  # x du point d’arrivée bord droit du canvas
            ligne,          # y du point d’arrivée   
            fill='gray20'   # couleur de la ligne (gris foncé)
        )   

def dessiner():
    """Dessine le serpent et la pomme sur le canvas."""
    canvas.delete('all')
    dessiner_grillage()
    
    # Dessiner le serpent en vert
    for i, (x, y) in enumerate(serpent):
        x1 = x * taille_case
        y1 = y * taille_case
        x2 = x1 + taille_case
        y2 = y1 + taille_case

        couleur = 'chartreuse3' if i == 0 else 'green'
        outline = 'chartreuse3' if i == 0 else 'darkgreen'
        canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline=outline)

    # Dessiner la pomme en rouge
    if pomme:
        x_pomme, y_pomme = pomme
        x1 = x_pomme * taille_case
        y1 = y_pomme * taille_case
        x2 = x1 + taille_case
        y2 = y1 + taille_case
        canvas.create_oval(
            x1 + 2, y1 + 2, x2 - 2, y2 - 2, fill='red', outline='black'
            )

def changer_direction(event):
    """Change la direction du serpent (empêche les demi-tours)."""
    global prochaine_direction
    
    touche = event.keysym
    
    if touche == "Up" and direction != SUD:
        prochaine_direction = NORD
    elif touche == "Down" and direction != NORD:
        prochaine_direction = SUD
    elif touche == "Left" and direction != EST:
        prochaine_direction = OUEST
    elif touche == "Right" and direction != OUEST:
        prochaine_direction = EST
    elif touche == "space":
        pause()

def boucle_jeu():
    """Boucle principale du jeu."""
    global serpent, direction, pomme, score, jeu_en_cours, prochaine_direction
    
    if not jeu_en_cours:
        return
    
    # Applique la direction
    direction = prochaine_direction
    
    # Vérifie si le serpent mange la pomme
    a_mange = (serpent[0] == pomme)
    
    serpent = deplacer_serpent(serpent, direction, a_mange)
    
    if collision_soi_meme(serpent):
        game_over()
        return
    
    elif collision_mur(serpent):
        game_over()
        return
    
    
    # Si le serpent a mangé
    if a_mange:
        score += 10
        label_score.config(text=f"Score: {score}")
        pomme = placer_pomme()
    
    # Redessine
    dessiner()
    
    fenetre.after(150, boucle_jeu)

def nouvelle_partie():
    """Démarre une nouvelle partie."""
    global serpent, direction, prochaine_direction, pomme, score, jeu_en_cours
    
    serpent = init_serpent()
    direction = EST
    prochaine_direction = EST
    pomme = placer_pomme()
    score = 0
    label_score.config(text=f"Score: {score}")
    jeu_en_cours = True
    dessiner()
    boucle_jeu()



def game_over():
    """Fin de partie."""
    global jeu_en_cours, meilleur_score
    
    jeu_en_cours = False
    
    # Mettre à jour le meilleur score
    if score > meilleur_score:
        meilleur_score = score
        label_meilleur.config(text=f"Meilleur Score: {meilleur_score}")
    
    # Message de Game Over
    messagebox.showinfo(
        "Game Over", #Titre de la fenetre
        f"Partie terminée !\n\nScore : {score}\nMeilleur score : {meilleur_score}"
    )


fenetre = tk.Tk()
fenetre.title("Jeu du Serpent - Snake")
fenetre.resizable(False, False)

frame_info = tk.Frame(fenetre, bg='black')
frame_info.pack()

# Affichage du score
label_score = tk.Label(
    frame_info, 
    text=f"Score: {score}", 
    font=("Arial", 14, "bold"),
    bg='black',
    fg='white'
)
label_score.pack(side=tk.LEFT, padx=20, pady=5)

# Affichage du meilleur score
label_meilleur = tk.Label(
    frame_info, 
    text=f"Meilleur Score: {meilleur_score}", 
    font=("Arial", 14, "bold"),
    bg='black',
    fg='gold'
)
label_meilleur.pack(side=tk.LEFT, padx=20, pady=5)
canvas = tk.Canvas(
    fenetre, 
    width=taille_canvas, 
    height=taille_canvas, 
    bg='black',
    highlightthickness=0
)
canvas.pack()
frame_boutons = tk.Frame(fenetre, bg='black')
frame_boutons.pack()

# Bouton Nouvelle Partie
bouton_nouvelle = tk.Button(
    frame_boutons, 
    text="Nouvelle Partie", 
    command=nouvelle_partie, 
    font=("Arial", 12, "bold"),
    bg='green',
    fg='white',
    padx=20,
    pady=5
)
bouton_pause = tk.Button(
    frame_boutons, 
    text="Mettre en Pause", 
    command=pause, 
    font=("Arial", 12, "bold"),
    bg='green',
    fg='white',
    padx=20,
    pady=5
)
bouton_nouvelle.pack(side=tk.LEFT, padx=10, pady=10)
bouton_pause.pack(side=tk.LEFT, padx=10, pady=10)
fenetre.bind("<Key>", changer_direction)
serpent = init_serpent()
pomme = placer_pomme()
dessiner()
fenetre.mainloop()