import math

# Cette classe contient deux fonctions pour évaluer la sécurité d'un mot de passe :
# l'une calcule son entropie, l'autre évalue sa force.
class PasswordTester:
    @staticmethod

    # Fonction qui calcule l'entropie d'un mot de passe.
    def calculate_entropy(password):
        alphabet_size = 0

        # Vérifie si le mot de passe contient au moins une minuscule.
        # Si oui, 26 est ajouté à la taille de l'alphabet.
        if any(c.islower() for c in password):
            alphabet_size += 26
        # Vérifie si le mot de passe contient au moins une majuscule.
        # Si oui, 26 est ajouté à la taille de l'alphabet.
        if any(c.isupper() for c in password):
            alphabet_size += 26
        # Vérifie si le mot de passe contient au moins un chiffre.
        # Si oui, 10 est ajouté à la taille de l'alphabet.
        if any(c.isdigit() for c in password):
            alphabet_size += 10
        # Vérifie si le mot de passe contient au moins un caractère spécial.
        # Si oui, 32 est ajouté à la taille de l'alphabet.
        if any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password):
            alphabet_size += 32

        # Calcule l'entropie du mot de passe avec la formule :
        # longueur_du_mot_de_passe × log2(taille_de_l_alphabet).
        # Exemple : un mot de passe de 16 caractères contenant des minuscules,
        # des majuscules, des chiffres et des caractères spéciaux donne :
        # taille de l'alphabet = 26 + 26 + 10 + 32 = 96
        # entropie = 16 × log2(96) = 104.87
        entropy = len(password) * math.log2(alphabet_size)
        return entropy

    # Fonction qui évalue la force du mot de passe selon son entropie :
    # "Faible" pour une entropie < 50, "Moyenne" pour 50 ≤ entropie < 80,
    # et "Forte" pour une entropie ≥ 80.
    @staticmethod
    def test_password_strength(password):
        entropy = PasswordTester.calculate_entropy(password)
        if entropy < 50:
            return "Faible"
        elif entropy < 80:
            return "Moyenne"
        else:
            return "Forte"
