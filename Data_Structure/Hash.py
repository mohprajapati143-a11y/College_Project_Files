# Simple Hash Table using Chaining

# Hash Table size
SIZE = 5

# Initialize table with empty lists
hash_table = [[] for _ in range(SIZE)]

# Hash function
def hash_function(key):
    return key % SIZE

# Insert a key
def insert(key):
    index = hash_function(key)
    hash_table[index].append(key)
    print(f"Inserted {key} at index {index}")

# Search a key
def search(key):
    index = hash_function(key)
    if key in hash_table[index]:
        print(f"Key {key} found at index {index}")
    else:
        print(f"Key {key} not found")

# Delete a key
def delete(key):
    index = hash_function(key)
    if key in hash_table[index]:
        hash_table[index].remove(key)
        print(f"Key {key} deleted from index {index}")
    else:
        print(f"Key {key} not found to delete")

# Display hash table
def display():
    print("\nHash Table:")
    for i, lst in enumerate(hash_table):
        print(f"{i}: {lst}")

# Practical Demo
insert(10)
insert(15)
insert(20)
insert(25)
insert(7)

display()

search(15)
search(100)

delete(20)
delete(50)

display()
