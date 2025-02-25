#Update the first set with items that don’t exist in the second set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 -= set2  # This will update set1 to contain only items not in set2
print(set1)  # Output: {1, 2}
