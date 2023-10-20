import tkinter as tk
import server
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame

# Fonction qui sera appelée lorsque le bouton est cliqué
def bouton_clique():
    print("Le serveur est sur écoute... Patientez un moment")
    server.receive()

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("600x600")  # Définir la taille de la fenêtre

# Personnaliser les couleurs
fenetre.configure(bg="#F3F3F3")  # Couleur de fond

# Initialiser Pygame pour la musique
pygame.mixer.init()
pygame.mixer.music.load("never.mp3")  # Remplacez "votre_musique.mp3" par le chemin de votre fichier audio
pygame.mixer.music.set_volume(0.9)  # Réglez le volume (facultatif)
pygame.mixer.music.play(-1)  # "-1" signifie que la musique se répétera en boucle

# Afficher un GIF animé au milieu
image = Image.open("dance.gif")  # Remplacez "votre_gif.gif" par le chemin de votre GIF animé
photo = ImageTk.PhotoImage(image)
gif_label = tk.Label(fenetre, image=photo, bg="#F3F3F3")
gif_label.image = photo
gif_label.place(relx=0.5, rely=0.5, anchor="center")

# Personnaliser le bouton
cadre = tk.Frame(fenetre, bg="#E0E0E0")  # Couleur de fond du cadre
cadre.place(relx=0.5, rely=0.9, anchor="s")  # Déplacer vers le bas

bouton = tk.Button(cadre, text="Cliquez-moi", command=bouton_clique, bg="#4CAF50", fg="white", font=("Helvetica", 16), bd=5, relief=tk.RAISED)
bouton.pack(padx=10, pady=10)

# Créer une étiquette vide
label = tk.Label(fenetre, text="")
label.pack()

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
