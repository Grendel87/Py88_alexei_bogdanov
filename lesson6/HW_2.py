from datetime import datetime


def func_decorator(fn):
    def new_func(m, n):
        current_time = datetime.now()
        print(fn(m, n))
        new_time = datetime.now()
        print(f"Функция {fn.__name__} отработала за {new_time - current_time} мс")

    return new_func


@func_decorator
def func1(a, b):
    return a + b


@func_decorator
def func2(a, b):
    return a * b


x = 1
y = 2
z = 3

func1(x, y)
func2(x, y)
