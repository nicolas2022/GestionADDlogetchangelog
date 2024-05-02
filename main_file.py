import customtkinter as ctk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPException, SMTPAuthenticationError
from datetime import datetime

# Configuration de l'apparence de l'interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Dictionnaire des identifiants et mots de passe historiques
historique_password = {"Nicolas": [("motdepasse", datetime.now()),
                                   ("MDP", datetime.now()),
                                   ("123", datetime.now())]}


class GestionADD:
    def __init__(self):
        self.interface_de_connexion = None
        self.username_entry = None
        self.password_entry = None
        self.show_button_password = None
        self.logiciel = None

    def open_main_window(self):
        if self.interface_de_connexion:
            self.interface_de_connexion.destroy()

        self.logiciel = ctk.CTk()
        self.logiciel.title("Gestion des ADD")
        self.logiciel.geometry("900x600")

        welcome_label = ctk.CTkLabel(self.logiciel, text="Bienvenue dans Gestion des ADD", font=("Helvetica", 20))
        welcome_label.pack(pady=20)

        logout_button = ctk.CTkButton(self.logiciel, text="Déconnexion", command=self.close_application)
        logout_button.pack(pady=10)

        self.logiciel.mainloop()

    def close_application(self):
        if self.logiciel:
            self.logiciel.destroy()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in historique_password:
            if password == historique_password[username][-1][0]:
                self.open_main_window()
            else:
                messagebox.showerror("Erreur de connexion", "Mot de passe incorrect.")
        else:
            messagebox.showerror("Erreur de connexion", "Identifiant incorrect.")

    def forgot_password(self):
        try:
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_email = "mail.test.nicolas.bertolini@gmail.com"
            receiver_email = "mail.test.nicolas.bertolini@gmail.com"
            # Mot de passe SMTP inscrit en clair dans le code
            password = "apho myrg hijz fgcj"

            message = MIMEText("Cliquez sur ce lien pour changer votre mot de passe : C:/01 Logiciel Python/changelog.py")
            message['Subject'] = "Réinitialisation du mot de passe"
            message['From'] = sender_email
            message['To'] = receiver_email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())

            messagebox.showinfo("Mot de passe oublié",
                                "Un email a été envoyé avec un lien pour réinitialiser votre mot de passe.")

        except SMTPAuthenticationError:
            messagebox.showerror("Erreur", "Authentification SMTP échouée. Veuillez vérifier vos identifiants Gmail.")
        except SMTPException as e:
            messagebox.showerror("Erreur", f"Une erreur SMTP s'est produite : {e}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'envoi de l'email : {e}")

    def toggle_visibility_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.configure(show="")
            self.show_button_password.configure(text="Masquer")
        else:
            self.password_entry.configure(show="*")
            self.show_button_password.configure(text="Afficher")

    def on_username_entry_return(self, event):
        self.password_entry.focus_set()

    def on_password_entry_return(self, event):
        self.login()

    def open_login_window(self):
        self.interface_de_connexion = ctk.CTk()
        self.interface_de_connexion.title("Gestion des ADD - Connexion")
        self.interface_de_connexion.geometry("400x300")
        self.interface_de_connexion.resizable(False, False)

        username_label = ctk.CTkLabel(self.interface_de_connexion, text="Identifiant:")
        username_label.pack(pady=5, padx=12)
        self.username_entry = ctk.CTkEntry(self.interface_de_connexion, width=300)
        self.username_entry.pack()
        self.username_entry.bind("<Return>", self.on_username_entry_return)

        password_label = ctk.CTkLabel(self.interface_de_connexion, text="Mot de passe:")
        password_label.pack(pady=5, padx=12)
        self.password_entry = ctk.CTkEntry(self.interface_de_connexion, show="*")
        self.password_entry.pack()

        # Bouton "Afficher/Masquer" pour le champ de mot de passe
        self.show_button_password = ctk.CTkButton(self.interface_de_connexion, width=40, height=10, font=("", 8),
                                                  text="Afficher", command=self.toggle_visibility_password)
        self.show_button_password.pack(pady=5, padx=12)

        self.password_entry.bind("<Return>", self.on_password_entry_return)

        login_button = ctk.CTkButton(self.interface_de_connexion, text="Connexion", command=self.login)
        login_button.pack(pady=25, padx=12)

        forgot_password_button = ctk.CTkButton(self.interface_de_connexion, fg_color="transparent",
                                               hover_color="grey", text="Mot de passe oublié",
                                               command=self.forgot_password)
        forgot_password_button.pack(pady=25, padx=12)


# Création de l'instance de la classe GestionADD et ouverture de la fenêtre de connexion
gestion_add = GestionADD()
gestion_add.open_login_window()

# Boucle pour maintenir l'application active
gestion_add.interface_de_connexion.mainloop()
