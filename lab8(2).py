#Create a new set from unique items from two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

unique_items = set1 ^ set2
print(unique_items)  # Output: {1, 2, 5, 6}
