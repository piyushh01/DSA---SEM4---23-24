set1 = set()
set2 = set()

# Get the total number of elements for set1 and set2
total1 = int(input("Enter the total elements of the set1 max(10): "))
total2 = int(input("Enter the total elements of the set2 : "))

# Input elements for the first set
print("Enter the elements of the first set")
for i in range(0, total1):
    elem1 = int(input("Enter the element : "))
    if elem1 < 0:
        print("You cannot insert negative elements in the set..")
        break
    set1.add(elem1)
    if len(set1) >= 10:
        print("Elements cannot be inserted more than 10")
        break
print("Set1:", set1)

# Input elements for the second set
print("Enter the elements of the second set")
for i in range(0, total2):
    elem2 = int(input("Enter the element : "))
    set2.add(elem2)
    if elem2 < 0:
        print("You cannot insert negative elements in the set..")
        break  # Add a break here to match the logic of set1 input

# Main operations loop
while True:  # No need for the 'flg' variable
    # Display menu options
    print("\n--- Set Operations Menu ---") 
    print("0. Add Element")
    print("1. Union")
    print("2. Intersection")
    print("3. Difference")
    print("4. Remove element")
    print("5. Subset")
    print("6. Superset")
    print("7. Disjoint")
    print("8. Size")
    print("9. Print the sets")
    print("10. Search")
    print("11. Exit")  # Add an exit option

    # Get user choice 
    while True:
        try:
            ch = int(input("Enter your choice: "))
            if 0 <= ch <= 11:  # Check for valid input range
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 11")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if ch == 0:
        # Add element to set1 or set2 based on user input
        elem = int(input("Enter the element to add : "))
        choice = int(input("Enter 1 to add in set1 and 2 in the set2 : "))
        if choice == 1:
            set1.add(elem)
        elif choice == 2:
            set2.add(elem)
        else:
            print("Invalid choice.")

    elif ch == 1:
        # Perform union operation and display the result
        union = set1.union(set2)
        print(f"Union is : {union}")

    if ch == 2:
# Perform intersection operation and display the result
intersection = set1.intersection(set2)
print(f"Intersection is : {intersection}")
opt = int(input("Enter 1 to continue, 0 to exit : "))
if opt == 0:
break
if ch == 3:
# Perform difference operation and display the result for both sets
difference1 = set1.difference(set2)
difference2 = set2.difference(set1)
print(f"Difference of set1 is : {difference1}")

    elif ch == 11:  # Exit
        print("Exiting the program")
        break
