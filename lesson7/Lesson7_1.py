str1 = input()
str2 = input()
str3 = input()
str4 = input()

with open("example.txt", "w") as f:
    f.write(str1)
    f.write("\n")
    f.write(str2)

f = open("example.txt", "a")
f.write("\n")
f.write(str3)
f.write("\n")
f.write(str4)
f.close
