import tkinter as tk
import server

# Fonction qui sera appelée lorsque le bouton est cliqué
def bouton_clique():
    print("Le serveur est sur écoute... Patientez un moment")
    server.receive()

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.geometry("200x200")  # Définir la taille de la fenêtre

# Créer un cadre pour centrer le bouton
cadre = tk.Frame(fenetre)
cadre.place(relx=0.5, rely=0.5, anchor="center")

# Créer un bouton dans le cadre
bouton = tk.Button(cadre, text="Cliquez-moi", command=bouton_clique)
bouton.pack()

# Créer une étiquette vide
label = tk.Label(fenetre, text="")
label.pack()

# Lancer la boucle principale de l'interface graphique
fenetre.mainloop()
