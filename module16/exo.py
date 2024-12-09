import  os
import shutil

x = open("MyFile.txt", "x")
x.close()

x = open("MyFile.txt", "a")
x.write("Here is line 1\n")
x.write("Here is line 2\n")
x.close()


src = "MyFile.txt"
dest = "CopyMyFile.txt"

shutil.copy(src, dest)

y = open("CopyMyFile.txt", "a")
y.write("Here is line 3\n")
y.write("Here is line 4\n")
y.write("Here is the copied file\n")
y.close()

x = open(src, "r")
y = open(dest, "r")

print("=============================here is the initial file========================================== \n")
print(x.read())
x.close()

print("=============================here is the copied file========================================== \n")
print(y.read())
y.close()