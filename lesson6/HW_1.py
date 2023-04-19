names = ("alex", "bil", "bob", "nik")

result = filter(lambda x: x == x[::-1], names)
print(tuple(result))
