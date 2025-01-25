import random
from qcm import questions

def main():
    # Mélanger les questions
    random.shuffle(questions)

    # Initialisation du score et des réponses de l'utilisateur
    score = 0
    user_answers = []  # Stocke les réponses de l'utilisateur

    # Boucle pour poser les questions
    for index, q in enumerate(questions, start=1):
        q.melanger_reponses()  # Mélanger les options avant d'afficher la question
        print(f"\nQuestion {index}:")
        q.afficher()

        # Récupérer la réponse de l'utilisateur
        reponse = input("Votre réponse (a, b ou c) : ")
        user_answers.append((q.question, reponse, q.correct))  # Stocke la question, la réponse et la bonne réponse

        if q.verifier_reponse(reponse):
            print("Bonne réponse ! ✅")
            score += 1
        else:
            print("Mauvaise réponse ❌")

    # Afficher le score final
    print(f"\nVotre score final est : {score} / {len(questions)}")

    # Afficher le corrigé
    print("\n=== Corrigé ===")
    for index, (question, user_answer, correct_answer) in enumerate(user_answers, start=1):
        print(f"Question {index}: {question}")
        print(f"Votre réponse : {user_answer} {'✅' if user_answer == correct_answer else '❌'}")
        print(f"Bonne réponse : {correct_answer}\n")

if __name__ == "__main__":
    main()
