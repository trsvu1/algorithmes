# Program 8 : 
# Écrire une fonction qui permet d'initialiser une matrice. 
# La fonction prend en argument une matrice (définie comme à l'exercice précédent), 
# ses dimensions et la valeur initiale à insérer dans chaque case de la matrice.

# Function
def matrix(rows, cols, value):

    matrix = [[value for i in range(rows)] for i in range(cols)]
    return matrix

# Main
value = int(input("Enter the value you want to init: "))
rows = int(input("Enter the rows of the matrix: "))
cols = int(input("Enter the cols of the matrix: "))

Matrix = matrix(rows, cols, value)

print(f"\nMatrix:")
for line in Matrix:
   print(line)

