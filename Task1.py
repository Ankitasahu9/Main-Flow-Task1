# Creating a list
my_list = [1, 2, 3, 4]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(5)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[1] = 10  # Changing the second element
print("List after modifying an element:", my_list)


# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("\nOriginal dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict["profession"] = "Engineer"
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
my_dict.pop("age")
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict["city"] = "San Francisco"
print("Dictionary after modifying a value:", my_dict)


# Creating a set
my_set = {1, 2, 3, 4}
print("\nOriginal set:", my_set)

# Adding an element to the set
my_set.add(5)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Modifying a set (not directly possible, but we can remove and add elements)
my_set.discard(4)  # Removing an element
my_set.add(6)      # Adding a new element
print("Set after modifying elements:", my_set)
      