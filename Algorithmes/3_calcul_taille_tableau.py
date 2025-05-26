# Program 3 : 
# Ecrire une fonction qui calcule la taille d'un tableau

# Fonction
def caculate_size(Table, begin_range, end_range):
    size = end_range - begin_range + 1
    return size

# Main
Table = [0] * 10
print(f"Bang : ",Table)
print(f"Kick thuoc cua bang la : ", caculate_size(Table, 1, 10))

