n = 0
while n <= 0:
    n = int(input("Enter the number of elements to be added to the list (should be greater than 0): "))

# Initializing an empty list
list_a = []

# Reading elements and adding them to the list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    list_a.append(element)

# Displaying the elements of the list in reverse
for i in range(1, n + 1):
    print(f"list_a[-{i}] = {list_a[-i]}")



### [1,  2,  3,  4,  5,  6,  7,  8, 9, 10]
### [0,  1,  2,  3,  4,  5,  6,  7, 8, 9]  indices positivos 
### [-10, -9, -8, -7, -6, -5, -4,-3,-2,-1] indices negativos

print(f"El último valor de la lista es: {list_a[-1]}")
print (f"El primer valor de la lista es: {list_a[-10]}")

