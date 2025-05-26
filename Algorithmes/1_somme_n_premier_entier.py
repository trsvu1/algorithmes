# Program 1 : 
# Ecrire une fonction qui calcule la somme des n premiers entiers naturels

# Fonction
def somme_n_premier_entier(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i
    return somme

# Main
entier = int(input("Donne un nombre entier : "))
print(f"Tong cac so tu 1 den {entier} la : {somme_n_premier_entier(entier)}")





































# def somme_n_premiers_entiers(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum
# 
# # Test de la fonction
# if __name__ == "__main__":
#     num = int(input("Entrez un entier n : "))
# 
#     while num < 0:
#         print("Veuillez donner un entier positif")
#         num = int(input("Entrez un entier n : "))
#     
#     print(f"La somme des {num} premiers entiers est : {somme_n_premiers_entiers(num)}")