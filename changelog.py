import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def change_password():
    new_password = new_password_entry.get()
    repeat_password = repeat_password_entry.get()

    if new_password == repeat_password:
        if len(new_password) < 10 or len(new_password) > 20:
            messagebox.showerror("Erreur", "Le mot de passe doit contenir entre 10 et 20 caractères, au moins une majuscule, une minuscule, un chiffre et un caractère spécial.")
        else:
            majuscule = False
            minuscule = False
            chiffre = False
            special = False

            for i in range(len(new_password)):
                if new_password[i] >= "a" and new_password[i] <= "z":
                    minuscule = True

                if new_password[i] >= "A" and new_password[i] <= "Z":
                    majuscule = True

                if new_password[i] >= "0" and new_password[i] <= "9":
                    chiffre = True

                if new_password[i] in ["²", "~", "#", "{", "(", "[", "-", "|", "_", "^", "@", ")", "°", "]", "+", "=", "}", "£",
                                    "$", "¤", "%", "µ", "*", "?", ",", ".", ";", "/", ":", "§", "!", "<", ">", "¨"]:
                    special = True

            if not (minuscule and majuscule and chiffre and special):
                messagebox.showerror("Erreur", "Le mot de passe doit contenir entre 10 et 20 caractères, au moins une majuscule, une minuscule, un chiffre et un caractère spécial.")
            else:
                # Mettre ici le code pour changer le mot de passe
                messagebox.showinfo("Mot de passe changé", "Le mot de passe a été modifié avec succès.")
    else:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")


def move_to_repeat_password(event):
    repeat_password_entry.focus_set()


def call_change_password(event):
    change_password()


def toggle_visibility_new_password():
    if new_password_entry.cget("show") == "*":
        new_password_entry.configure(show="")
        show_button_new_password.configure(text="Masquer")
    else:
        new_password_entry.configure(show="*")
        show_button_new_password.configure(text="Afficher")


def toggle_visibility_repeat_password():
    if repeat_password_entry.cget("show") == "*":
        repeat_password_entry.configure(show="")
        show_button_repeat_password.configure(text="Masquer")
    else:
        repeat_password_entry.configure(show="*")
        show_button_repeat_password.configure(text="Afficher")


# Créer la fenêtre principale
window = ctk.CTk()
window.title("Changement de mot de passe")
window.geometry("400x260")
window.resizable(False, False)

# Champ pour le nouveau mot de passe
new_password_label = ctk.CTkLabel(window, text="Nouveau mot de passe :")
new_password_label.pack(pady=5, padx=12)
new_password_entry = ctk.CTkEntry(window, show="*")
new_password_entry.pack(pady=5, padx=12)
new_password_entry.bind("<Return>", move_to_repeat_password)  # Lier la touche "Entrée"

# Bouton "Afficher/Masquer" pour new_password_entry
show_button_new_password = ctk.CTkButton(window, width=40, height=10, font=("",8), text="Afficher", command=toggle_visibility_new_password)
show_button_new_password.pack()

# Champ pour répéter le nouveau mot de passe
repeat_password_label = ctk.CTkLabel(window, text="Confirmer le mot de passe :")
repeat_password_label.pack(pady=5, padx=12)
repeat_password_entry = ctk.CTkEntry(window, show="*")
repeat_password_entry.pack(pady=5, padx=12)
repeat_password_entry.bind("<Return>", call_change_password)  # Lier la touche "Entrée"

# Bouton "Afficher/Masquer" pour repeat_password_entry
show_button_repeat_password = ctk.CTkButton(window, width=40, height=10, font=("",8), text="Afficher", command=toggle_visibility_repeat_password)
show_button_repeat_password.pack()

# Bouton pour changer le mot de passe
change_button = ctk.CTkButton(window, text="Changer le mot de passe", command=change_password)
change_button.pack(pady=25)

# Lancer l'application
window.mainloop()