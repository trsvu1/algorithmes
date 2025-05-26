# Fonction
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_array(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr = [0] * (n1 + n2)

    i = i1 = i2 = 0

    for i in range(n1 + n2):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            i1 += 1
        else:
            arr[i] = arr2[i2]
            i2 += 1
    return arr

# Main

# Get input from user
arr1_input = input("\nEnter element for first array: ")
arr2_input = input("Enter element for second array: ")

# Convert input string into liste of integer
arr1 = [int(x) for x in arr1_input.split()]
arr2 = [int(x) for x in arr2_input.split()]

# Display user input array
print(f"\nUser input array 1:", arr1)
print(f"User input array 2:", arr2)

# Call function to sort 2 input array
bubble_sort(arr1)
bubble_sort(arr2)

# Display array being sorted
print(f"\nArray after sorted:", arr1)
print(f"Array after sorted:", arr2)

array = merge_array(arr1, arr2)

# Display final array
print(f"\nSorted merged array:,", array)
