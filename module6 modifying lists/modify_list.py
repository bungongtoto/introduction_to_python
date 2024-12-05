fruits = ["apple", "oranges", "banana", "grapes"]

# fruits += ["mangoes"]
#
# print(fruits)
#
# #using the insert() method
#
# fruits.insert(2, "berries")
# print(fruits)
#
#
# fruits.remove("grapes")
#
# print(fruits)

del fruits[2]

print(fruits)

for x in fruits:
    print(x)

if "banana" in fruits:
    print("Yes, banana is the list")
else:
    print("No, banana is not on the list")