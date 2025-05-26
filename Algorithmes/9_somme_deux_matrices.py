# Program 9 : 
# Écrire une fonction qui permet de faire la somme de deux matrices. 
# Cette fonction prend en argument deux matrices de même taille, leur dimension, elle renvoie une matrice.

# Function
def sum_2_matrix(M1, M2, rows, cols):
    matrix = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = M1[i][j] + M2[i][j]
    return matrix

# Main

M1 = [ [1,2,3],[4,5,6],[7,8,9] ]
M2 = [ [1,3,5],[7,9,11],[13,15,17] ]
rows = 3
cols = 3
Sum = sum_2_matrix(M1, M2, rows, cols)

print("\nMatrix 1:")
for line in M1: print(line)

print("\nMatrix 2:")
for line in M2: print(line)

print("\nSum 2 Matrix:")
for line in Sum: print(line)



