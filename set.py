set1 = set()
set2 = set()

# Get the total number of elements for set1 and set2
total1 = int(input("Enter the total elements of the set1 max(10): "))
total2 = int(input("Enter the total elements of the set2 : "))

# Flag for loop continuation
flg = 1

# Input elements for the first set
print("Enter the elements of the first set")
for i in range(0, total1):
    elem1 = int(input("Enter the element : "))
    # Check for negative elements in set1
    if elem1 < 0:
        print("You cannot insert negative elements in the set..")
        break
    set1.add(elem1)
    # Check if the set1 size exceeds 10
    if len(set1) >= 10:
        print("Elements cannot be inserted more than 10")
        break
print("Set1:", set1)

# Input elements for the second set
print("Enter the elements of the second set")
for i in range(0, total2):
    elem2 = int(input("Enter the element : "))
    set2.add(elem2)
    # Break loop if a negative element is encountered
    if elem2 < 0:
        break

while flg == 1:
    # Display menu options
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

    # User choice input
    ch = int(input("Enter your choice: "))
    if ch == 0:
        # Add element to set1 or set2 based on user input
        elem = int(input("Enter the element to add : "))
        choice = int(input("Enter 1 to add in set1 and 2 in the set2 : "))
        if choice == 1:
            set1.add(elem)
        else:
            set2.add(elem)
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 1:
        # Perform union operation and display the result
        union = set1.union(set2)
        print(f"Union is : {union}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
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
        print(f"Difference of set2 is : {difference2}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 4:
        # Remove element from set1 or set2 based on user input
        removeelem = int(input("Enter the element to remove : "))
        choice = int(input("Enter 1 to remove in set1 and 2 in the set2 : "))
        if choice == 1:
            set1.remove(removeelem)
        if choice == 2:
            set2.remove(removeelem)
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 5:
        # Check if set1 is a subset of set2
        print(f"Is SetA a subset of setB: {set1.issubset(set2)}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 6:
        # Check if set1 is a superset of set2
        print(f"Is SetA a superset of setB: {set1.issuperset(set2)}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 7:
        # Check if set1 and set2 are disjoint sets
        print(f"Is SetA a disjoint set: {set1.isdisjoint(set2)}")
        print(f"Is SetB a disjoint set: {set2.isdisjoint(set1)}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 8:
        # Display the size of set1 and set2
        print(f"Size of the set1 : {len(set1)}")
        print(f"Size of the set2 : {len(set2)}")
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 9:
        # Print elements of set1 and set2
        print("Elements in the set1 are : ")
        for element in set1:
            print(element)
        print("Elements in the set2 are : ")
        for element in set2:
            print(element)
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
    if ch == 10:
        # Search for an element in set1 or set2 based on user input
        elem = int(input("Enter the element to search : "))
        choice = int(input("Enter 1 to search in set1 and 2 in the set2 : "))
        if choice == 1:
            if elem in set1:
                print(True)
            else:
                print(False)
        if choice == 2:
            if elem in set2:
                print(True)
            else:
                print(False)
        opt = int(input("Enter 1 to continue, 0 to exit : "))
        if opt == 0:
            break
