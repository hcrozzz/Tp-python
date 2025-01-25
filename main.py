from password_generator import PasswordGenerator
from password_tester import PasswordTester
from passphrase_generator import PassphraseGenerator

if __name__ == "__main__":

    # Initialisation de la variable qui stockera le choix de l'utilisateur.
    choix = ""


# Boucle while qui continue d'exécuter le programme tant que l'utilisateur n'entre pas "q" pour quitter.
while choix != 'q':
    # Affichage des options disponibles : générer un mot de passe, générer une passphrase ou quitter le programme.
    print("###########################################")
    print("0 - Générateur de mot de passe")
    print("1 - Générateur de passphrase")
    print("q - Quitter")
    print("###########################################")

    # L'utilisateur saisit son choix d'outil.
    choix = input("Choix de l'outil : ")
    print("###########################################")

    # Si l'utilisateur choisit l'option 0, le programme exécute le générateur de mot de passe.
    if choix == "0":
        # Demande à l'utilisateur d'entrer les paramètres : 
        # nombre de minuscules, majuscules, chiffres et caractères spéciaux.
        lowerCases = int(input('Nombre de minuscules : '))
        upperCases = int(input('Nombre de majuscules : '))
        nbDigits = int(input('Nombre de chiffres : '))
        nbSpecials = int(input('Nombre de caractères spéciaux : '))

        # Création d'une instance de PasswordGenerator avec les paramètres spécifiés.
        generator = PasswordGenerator(lower=lowerCases, upper=upperCases, digits=nbDigits, specials=nbSpecials)

        # Génération du mot de passe avec les critères sélectionnés.
        password = generator.generate_password()

        # Affichage du mot de passe généré.
        print(f"Mot de passe généré : {password}")
               
        # Utilisation de PasswordTester pour calculer l'entropie et tester la force du mot de passe.
        tester = PasswordTester()
        entropy = tester.calculate_entropy(password)
        strength = tester.test_password_strength(password)

        # Affichage des résultats : entropie (en bits) et force du mot de passe.
        print(f"Entropie : {entropy:.2f} bits - Force : {strength}")
    
    # Si l'utilisateur choisit l'option 1, le programme exécute le générateur de passphrase.
    elif choix == "1":
        # Demande du nombre de mots souhaités pour la passphrase.
        nbWord = int(input("Nombre de mots de la passphrase : "))
        passphrase_gen = PassphraseGenerator()
        
        # Génération de la passphrase à partir du nombre de mots spécifié.
        passphrase = passphrase_gen.generate_passphrase(num_words=nbWord)

        # Affichage de la passphrase générée.
        print(f"Passphrase générée : {passphrase}")
    
    # Si l'utilisateur entre "q", le programme affiche un message de fin et s'arrête.
    elif choix == 'q':
        print("Arrêt du programme")
    
    # Si une option invalide est saisie, un message d'erreur est affiché.
    else:
        print("Choix invalide")
