a = int(input("Enter Array size: "))
for i in range(a):
    b = int(input("Enter Array element: "))
    if i == 0:
        arr = [b]
    else:
        arr.append(b)
print("Array is: ", arr)
sum = 0
for i in range(a):
    sum += arr[i]
print("Sum of all elements in the array is: ", sum)
print("Maximum element in the array is: ", max(arr))
print("Minimum element in the array is: ", min(arr))
arr.sort()
print("Sorted Array is: ", arr)
arr.reverse()
print("Reversed Array is: ", arr)
arr1 = arr.copy()
print("Copied Array is: ", arr1)
location = int(input("Enter the location of the element to be deleted: "))
if location < len(arr):
    del arr[location]
    print("Array after deletion is: ", arr)
