s = int(input("Enter the size of the stack: "))
stack = []
for i in range(s):
    stack.append(int(input(f"Enter the element{i}: ")))
print("The stack is: ", stack)
while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(stack) == s:
            print("Stack is full")
        else:
            element = int(input("Enter the element to push: "))
            stack.append(element)
            print("Element pushed:", element)
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            element = stack.pop()
            print("Element popped:", element)
    elif choice == 3:
        print("The stack is: ", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
