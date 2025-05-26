# Program 11 : 
# Écrire un algorithme de tri par fusion de deux tableaux. 
# La fonction prend en entrée deux tableaux non triés, leur longueur respective, 
# elle renvoie un tableau trié contenant les éléments des deux tableaux en entrée.

# Function
def sorted_merge_array(arr1, arr2):
    arr1_sorted = sorted(arr1)
    arr2_sorted = sorted(arr2)

    n1 = len(arr1_sorted)
    n2 = len(arr2_sorted)
    arr = [0] * (n1 + n2)

    i = i1 = i2 = 0

    for i in range(n1 + n2):
        if i1 < n1 and (i2 >= n2 or arr1_sorted[i1] <= arr2_sorted[i2]):
            arr[i] = arr1_sorted[i1]
            i1 += 1
        else:
            arr[i] = arr2_sorted[i2]
            i2 += 1
    return arr

# Main
arr1 = [7,0,2,1,3]
arr2 = [6,4,5,9,8]

print(f"\nArray 1:", arr1)
print(f"Array 2:", arr2)

array = sorted_merge_array(arr1, arr2)

arr1_sorted = sorted(arr1)
arr2_sorted = sorted(arr2)

print(f"\nArray 1:", arr1_sorted)
print(f"Array 2:", arr2_sorted)

print(f"\nSorted Merge Array:", array)


