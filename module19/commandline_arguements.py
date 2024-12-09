import sys

print("The name of your file is: ", (sys.argv[0]))

print("Then number arguments is: ", (len(sys.argv)))

for argument in sys.argv:
    print(argument)