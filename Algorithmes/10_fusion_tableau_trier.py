# Program 10 : 
# Écrire une fonction qui permet de fusionner deux tableaux triés, elle retourne le tableau trié contenant les éléments des deux tableaux en entrée. 
# Elle prend en entrée un tableau, sa longueur, un autre tableau, sa longueur ; elle renvoie un tableau.
# Cette nouvelle fonction doit avoir une complexité algorithmique aussi faible que possible.

# Function
def sorted_merge_arr(arr1, arr2):
    
    n1 = len(arr1)
    n2 = len(arr2)
    arr = [0] * (n1 + n2)

    i = i1 = i2 = 0
    
    for i in range(n1 + n2):
        if i1 < n1 and (i2 >= n2 or (arr1[i1] <= arr2[i2])):
            arr[i] = arr1[i1]
            i1 += 1
        else:
            arr[i] = arr2[i2]
            i2 += 1
    return arr

# Main
arr1 = [1,2,3]
arr2 = [4,5,6]

print(f"\nArray 1:", arr1)
print(f"Array 2:", arr2)

arr = sorted_merge_arr(arr1, arr2)

print(f"\nSorted Merge Array:", arr)




