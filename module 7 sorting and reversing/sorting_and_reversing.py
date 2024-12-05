colors: list[str] = ["Blue", "Red", "Yellow", "Green"]
print(colors)
print("----------------------------#sorts the colors from A to Z---------------------------------")
#sorts the colors from A to Z
colors.sort()
print(colors)

print("--------------------------------#sorts the colors from Z to A-----------------------------")
#sorts the colors from Z to A
colors.sort(reverse=True)
print(colors)

print("--------------------------------#reverse the order of the List-----------------------------")
#reverse the order of the List

colors.reverse()
print(colors)

colors: list[str] = ["Blue", "Red", "Yellow", "Green", "Pink"]

print("Here is the first List")
print(colors)

print("\nHere is a sorted List")
print(sorted(colors))

print(colors)