#Trapping error

txt = input("Give me a number please: ")

try:
    num = int(input(txt))
    print("The number you gave is: " , num)
except ValueError:
    print("Please put in a real number, not a string or a text.")