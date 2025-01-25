import random

# Classe qui contient la structure nécessaire pour générer une passphrase 
# ainsi que la fonction permettant de la créer.
class PassphraseGenerator:

    # Préparation de la génération de la passphrase.
    # Le fichier de la liste de mots ("eff_large_wordlist") est ouvert en mode lecture.
    def __init__(self, word_list_file="eff_large_wordlist.txt"):
        with open(word_list_file, 'r') as f:
            # La liste de mots est construite en extrayant le deuxième élément 
            # de chaque ligne (le mot) et en supprimant les espaces inutiles.
            self.word_list = [line.strip().split()[1] for line in f]

    # Fonction permettant de sélectionner aléatoirement un certain nombre de mots
    # dans la liste (par défaut 5) et de les assembler en une passphrase.
    def generate_passphrase(self, num_words=5):
        return ' '.join(random.choices(self.word_list, k=num_words))
