import random
import string

NIVEAUX = {
    1: ("facile", 20),
    2: ("moyen", 15),
    3: ("difficile", 10)
}

def welcome_page():
    print("Bienvenue sur le jeu de deviner le caractère")
    print("Je pense à un caractère de (a - z) et si tu peux le trouver, tu gagnes 100 euros")
    print("Tout d'abord, choisis le niveau du jeu")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")

def main():
    welcome_page()
    level = int(input("Choisis le niveau du jeu par son numéro : "))
    niveau, essais = NIVEAUX.get(level, NIVEAUX[2])
    print(f"Tu as choisi le niveau {niveau}, tu as {essais} essais")

    win = random.choice(string.ascii_lowercase)
    count = 0

    while count < essais:
        character = input("Tape ton caractère : ").lower()
        if character == win:
            print("Bravo! Tu as gagné 100 euros")
            break
        else:
            print("Ce n'est pas le bon caractère, réessaye : ")
            count += 1
    else:
        print("Désolé, tu as perdu")
        print(f"Le caractère était {win}")

if __name__ == "__main__":
    main()
