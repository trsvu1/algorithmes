# Program 12 : 
# Écrire une fonction qui permet de recherche d'un élément dans un tableau d'entiers. 
# La fonction prend en argument un tableau, sa longueur, ainsi que l'élément à chercher ; elle renvoie un indice.

# Function
def find_element(Table, table_length, element_to_find):

    for i in range(table_length):
        if Table[i] == element_to_find:
            return i
    return None
            
# Main
Table = [9,6,5,1,2,4,5]
table_length = 6
element_to_find = 4

print(f"\nTable:", Table)
print(f"Searching for:", element_to_find)

result = find_element(Table, table_length, element_to_find)

print(f"\nThe position of {element_to_find} in the table: ", result)





