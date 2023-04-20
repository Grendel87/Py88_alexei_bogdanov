str1 = input()
str2 = input()
str3 = input()
str4 = input()

with open("example.txt", "w") as f:
    f.write("str1\nstr2")

f = open("example.txt", "a")
f.write("\nstr3\nstr4")
f.close
