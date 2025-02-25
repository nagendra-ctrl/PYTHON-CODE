#Update set1 by adding items from set2, except common items
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.update(set2 - set1)  # Add items from set2 that are not in set1
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

