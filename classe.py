import random

class Question:
    def __init__(self, question, options, correct):
        self.question = question
        self.options = options
        self.correct = correct

    def melanger_reponses(self):
        """Mélange les options et met à jour l'index de la bonne réponse."""
        correct_option = self.options[ord(self.correct) - ord('a')]  # Trouver la réponse correcte dans les options
        random.shuffle(self.options)  # Mélanger les options
        self.correct = chr(self.options.index(correct_option) + ord('a'))  # Mettre à jour `self.correct` avec la nouvelle position

    def afficher(self):
        """Affiche la question et les options."""
        print(self.question)
        for option in self.options:
            print(option)

    def verifier_reponse(self, reponse):
        """Vérifie si la réponse est correcte (sensible à la casse)."""
        return reponse == self.correct
