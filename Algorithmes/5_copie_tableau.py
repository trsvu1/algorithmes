# Program 5 : 
# Écrire une fonction qui permet de faire la copie d'un tableau. 
# Cette fonction prend en entrée deux tableaux de même longueur, leur longueur, l'indice à partir duquel les données doivent être copiées,
# le dernier indice qui doit être copié et le premier indice où insérer des données dans le deuxième tableau.

# Fonction
def copy_Table(Table1, Table2, begin_range, end_range, copy_position):
    for i in range (begin_range, end_range + 1):
        Table2[copy_position + ( i - begin_range )] = Table1[i]

# Main
Table1 = [0,1,2,3,4,5]
Table2 = [0,0,0,0,0,0]

print("\nBefore Copy")
print(f"Table1:", Table1)
print(f"Table2:", Table2)

copy_Table(Table1, Table2, 2, 4, 3)

print("\nAfter Copy")
print(f"Table1:", Table1)
print(f"Table2:", Table2)




