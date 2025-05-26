# Program 6 : 
# Écrire une fonction qui permet de connaître l'indice du premier élément minimum d'un tableau. \
# La fonction prend en argument un tableau d'entiers et sa longueur, elle renvoie la valeur minimum dans le tableau.

# Function
def find_minimum(Table, length):
    min_value = Table[0]
    for i in range (length):
        if Table[i] < min_value:
            min_value = Table[i]
    return min_value

# Main
Table_input = input("\nEnter the element in the array: ")
Table = [int(x) for x in Table_input.split()]

print(f"\nTable:", Table)

length = int(input("In what range you want to find: "))
result = find_minimum(Table, length)

print(f"\nThe smallest value in table is:", result)



