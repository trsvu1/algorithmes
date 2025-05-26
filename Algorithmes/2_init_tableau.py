# Program 2 : 
# Écrire une fonction qui permet d'initialiser un tableau. 
# Cette fonction prend en entrée un tableau, sa longueur et une valeur à insérer dans chacune des cases du tableau.

# Fonction
def init_Tableau(tableau, longeur, valeur):
    for i in range (longeur):
        tableau[i] = valeur
    
# Main
Tableau = [0] * 10
print(f"Tableau avant init :", Tableau)

init_Tableau(Tableau, 10, 3)
print(f"Tableau apres init :", Tableau)

