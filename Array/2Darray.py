r = int(input("Enter a value for row: "))
c = int(input("Enter a value for column: "))
arr = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"Enter value for element [{i}][{j}]: ")))
    arr.append(row)
print("The 2D array is:")
for i in range(r):
    for j in range(c):
        print(arr[i][j], end=" ")
    print()
# Calculate the sum of all elements in the 2D array
sum = 0
for i in range(r):
    for j in range(c):
        sum += arr[i][j]
print("The sum of all elements in the 2D array is:", sum)
# Copy the 2D array
arr1 = arr.copy()
print("The copied 2D array is:")
for i in range(r):
    for j in range(c):
        print(arr1[i][j], end=" ")
    print()
# Find the maximum and minimum elements in the 2D array
print("The maximum element in the 2D array is:", max(max(row) for row in arr))
print("The minimum element in the 2D array is:", min(min(row) for row in arr))
# Sort the 2D array
arr.sort()
print("The sorted 2D array is:")
for i in range(r):
    for j in range(c):
        print(arr[i][j], end=" ")
    print()
# Reverse the 2D array
arr.reverse()
print("The reversed 2D array is:")
for i in range(r):
    for j in range(c):
        print(arr[i][j], end=" ")
    print()