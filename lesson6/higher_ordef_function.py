def func1():
    """
    Lesson1
    """
    return func1.__name__


def func2():
    """
    Lesson2
    """
    return func2.__name__


def func3():
    """
    Lesson3
    """
    return func3.__name__


# ---------------------------------------------------------------------------------------------------------------------


def repeat(fn, n=10):
    for i in range(n):
        print(f"{fn()} {i + 1}")


repeat(func1, 3)
repeat(func2, 5)
repeat(func3)
