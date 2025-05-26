# Exercice 1 : Calculer la hauteur d'un arbre en vous basant sur la définition récursive :
# - un arbre vide est de hauteur 0 ;
# - un arbre non vide a pour hauteur 1 + la hauteur maximale entre ses fils.

# Définition de la classe Noeud pour représenter un arbre général (n-aire)
class Noeud:
    def __init__(self, valeur, enfants=None):
        self.valeur = valeur
        self.enfants = enfants if enfants is not None else []

# Fonction récursive pour calculer la hauteur de l’arbre
def hauteur_arbre(noeud):
    if noeud is None:
        return 0
    if not noeud.enfants:  # Si le nœud n’a pas d’enfants
        return 1
    # Calcul récursif sur tous les enfants
    return 1 + max(hauteur_arbre(enfant) for enfant in noeud.enfants)

# Exemple d’arbre :
#         A
#       / | \
#      B  C  D
#         |   
#         F    

# Création des nœuds
d = Noeud("D")
f = Noeud("F")
c = Noeud("C", [f])
b = Noeud("B")
a = Noeud("A", [b, c, d])  # Racine avec 3 enfants

# Calcul et affichage de la hauteur
print("Hauteur de l'arbre :", hauteur_arbre(a))  # Résultat attendu : 3