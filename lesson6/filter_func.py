names = ("Alexei", "Bil", "Carl", "Fiona")

def filter_tuple(tpl, greater_4 = True):
    return tuple(filter(lambda x: 4 < len(x) if greater_4 else len(x) <= 3, tpl))

print(filter_tuple(names))
print(filter_tuple(names, greater_4 = False))