numbers = [1, 2, 3, 4, 5]


def check_list(num):
    return dict(map(lambda x: (x, "Чётное" if x % 2 == 0 else "Нечётное"), num))


print(check_list(numbers))
