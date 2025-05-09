r1 = int(input("Enter a value for row1: "))
c1 = int(input("Enter a value for column1: "))
arr1 = []
for i in range(r1):
    row1 = []
    for j in range(c1):
       row1.append(int(input(f"Enter value for element [{i}][{j}]: ")))
    arr1.append(row1)
print("The Array is:")
for i in range(r1):
    for j in range(c1):
        print(arr1[i][j], end=" ")
    print()
    
r2 = int(input("Enter a value for row2: "))
c2 = int(input("Enter a value for column2: "))
arr2 = []
for i in range(r2):
    row2 = []
    for j in range(c2):
        row2.append(int(input(f"Enter value for element [{i}][{j}]: ")))
    arr2.append(row2)
print("The Array is:")
for i in range(r2):
    for j in range(c2):
        print(arr2[i][j], end=" ")
    print()
# Calculate the sum of two array
arr4 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(arr1[i][j] + arr2[i][j])
    arr4.append(row)
print("The sum of two array is:")
for i in range(r1):
    for j in range(c1):
        print(arr4[i][j], end=" ")
    print()


# Copy the two array
arr1 = arr1.copy()
arr2 = arr2.copy()
print("The copied array1 is:")
for i in range(r1):
    for j in range(c1):
        print(arr1[i][j], end=" ")
    print()

print("The copied array2 is:")
for i in range(r2):
    for j in range(c2):
        print(arr2[i][j], end=" ")
    print()

# Find the multiplication of two array
arr3 = []
for i in range(r1):
    row = []
    for j in range(c2):
        sum = 0
        for k in range(c1):
            sum += arr1[i][k] * arr2[k][j]
        row.append(sum)
    arr3.append(row)
print("The multiplied array is:")
for i in range(r1):
    for j in range(c2):
        print(arr3[i][j], end=" ")
    print()