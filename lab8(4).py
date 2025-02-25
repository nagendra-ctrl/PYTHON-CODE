#Chcheck if two sets have any elements in common. If yes, display the common elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

common_elements = set1 & set2
if common_elements:
    print("Common elements:", common_elements)  # Output: Common elements: {3, 4}
else:
    print("No common elements.")
