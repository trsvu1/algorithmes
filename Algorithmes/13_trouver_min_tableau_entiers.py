# Program 13 : 
# Écrire une fonction qui permet de connaître le minimum d'un tableau d'entiers. 
# La fonction prend en entrée un tableau d'entiers, sa longueur et renvoie un élément du tableau.

# Function
def find_minimum(Table, range_search):
    min_value = Table[0]
    for i in range(range_search):
        if Table[i] < min_value:
            min_value = Table[i]
    return min_value

# Main
Table_input = input("Enter the element in the table: ")

Table = [int(x) for x in Table_input.split()]

print(f"\nTable: ", Table)

range_search = int(input("Range to search: "))

result = find_minimum(Table, range_search)

print(f"\nThe min value in the array is: ", result)




