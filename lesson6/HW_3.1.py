def check_string(string):
    if string.isdigit():
        return f"Вы ввели положительное целое число: {string}"
    for i in string:
        if "-0.123456789".find(i) == -1:
            return f"Вы ввели некорректное число: {string}"
    if string.count("-") > 1 or string.count(".") > 1 or string.find("-") > 0:
        return f"Вы ввели некорректное число: {string}"
    if string.find(".") != -1:
        if string.find("-") != -1:
            return f"Вы ввели отрицательное дробное число: {string}"
        else:
            return f"Вы ввели положительное дробное число: {string}"
    else:
        return f"Вы ввели отрицательное целое число: {string}"


print(check_string("1234"))
print(check_string("-1234"))
print(check_string("0.1234"))
print(check_string(".1234"))
print(check_string("-.1234"))
print(check_string(",1234"))
print(check_string("-,1234"))
print(check_string("f1234"))
print(check_string("1.2.34"))
print(check_string("1,2,34"))
print(check_string("1-234"))
print(check_string("1.2,34"))
print(check_string("-1-234"))
