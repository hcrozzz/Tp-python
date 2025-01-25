import random
import string

# Classe définissant la structure et les méthodes pour générer un mot de passe aléatoire
class PasswordGenerator:
    def __init__(self, lower=0, upper=0, digits=0, specials=0):
        self.lower = lower  # Nombre de lettres minuscules
        self.upper = upper  # Nombre de lettres majuscules
        self.digits = digits  # Nombre de chiffres
        self.specials = specials  # Nombre de caractères spéciaux
        self.special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/"  # Liste des caractères spéciaux disponibles

    # Génère un mot de passe aléatoire selon les critères définis (lower, upper, digits, specials)
    def generate_password(self):
        password = (
            random.choices(string.ascii_lowercase, k=self.lower) +  # Ajoute des lettres minuscules
            random.choices(string.ascii_uppercase, k=self.upper) +  # Ajoute des lettres majuscules
            random.choices(string.digits, k=self.digits) +          # Ajoute des chiffres
            random.choices(self.special_chars, k=self.specials)     # Ajoute des caractères spéciaux
        )

        # Mélange les caractères pour garantir un mot de passe sans structure prédictible
        random.shuffle(password)
        return ''.join(password)  # Retourne le mot de passe final sous forme de chaîne de caractères