# Program 4 : 
# Ecrire une fonction qui echange deux elements d'un tableau

# Fonction
def swap_value(Table, i, j):
    # Using x to swap the values in the array
    x = 0

    x = Table[i]
    Table[i] = Table[j]
    Table[j] = x

    return Table

# Main
Table = [7,2,4,6,7,1]
print(f"\nTable before value swap:", Table)

i = 2
j = 4
print(f"\nSwap the value {i} and {j}")

swap_value(Table, i, j)
print(f"\nTable after value swap:", Table)

