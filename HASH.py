TABLE_SIZE = 3
table = [None] * TABLE_SIZE

def hash_func(key):
    return key % TABLE_SIZE

def insert_linearprob(key, value):
    hash_val = hash_func(key)
    while table[hash_val] is not None and table[hash_val][0] != key:
        hash_val = (hash_val + 1) % TABLE_SIZE
    table[hash_val] = (key, value)
    print(table)

def insert_quadratic_prob(key, value):
    hash_val = hash_func(key)
    i = 1
    while table[hash_val] is not None and table[hash_val][0] != key:
        hash_val = (hash_val + i**2) % TABLE_SIZE
        i += 1
    table[hash_val] = (key, value)
    print(table)

def search(key):
    hash_val = hash_func(key)
    while table[hash_val] is not None and table[hash_val][0] != key:
        hash_val = (hash_val + 1) % TABLE_SIZE
    if table[hash_val] is None:
        return -1
    else:
        return table[hash_val][1]

def remove(key):
    hash_val = hash_func(key)
    while table[hash_val] is not None:
        if table[hash_val][0] == key:
            break
        hash_val = (hash_val + 1) % TABLE_SIZE
    if table[hash_val] is None:
        print(f"No Element found at key {key}")
    else:
        table[hash_val] = None
        print("Element Deleted")

while True:
    print("\n1.Linear Probing")
    print("\n2.Quadratic Hashing")
    type = int(input("Enter (1/2) to select way to perform hashing: "))
    print("\n----------------------")
    print("Operations on Hash Table")
    print("\n----------------------")
    print("1.Insert element into the table")
    print("2.Search element from the key")
    print("3.Delete element at a key")
    print("4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if type == 1:
            value = input("Enter element to be inserted: ")
            key = int(input("Enter key at which element to be inserted: "))
            insert_linearprob(key, value)
        elif type == 2:
            value = input("Enter element to be inserted: ")
            key = int(input("Enter key at which element to be inserted: "))
            insert_quadratic_prob(key, value)
    elif choice == 2:
        key = int(input("Enter key of the element to be searched: "))
        result = search(key)
        if result == -1:
            print(f"No element found at key {key}")
        else:
            print(f"Element at key {key} : {result}")
    elif choice == 3:
        key = int(input("Enter key of the element to be deleted: "))
        remove(key)
    elif choice == 4:
        break
    else:
        print("\nEnter correct option\n")
