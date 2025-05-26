# Program : 
# Write a program to find an element in an array
# The program that take input a table, it length and element to find
# Return his position in the table if found
# Return None if not

# Fonction
def find_element_position(Table, table_length, element_to_find):
    
    for i in range(table_length):
        if Table[i] == element_to_find:
            return i
    return None

# Main

Table = [3,7,5,9,1,2,6,4,0]

print(f"\nTable:", Table)
table_length = int(input("\nIn which range you want to find your element: "))
element_to_find = int(input("What element you want to find: "))

print(f"\nElement to find:", element_to_find)
result = find_element_position(Table, table_length, element_to_find)

print(f"\nThe position of {element_to_find} is:", result)