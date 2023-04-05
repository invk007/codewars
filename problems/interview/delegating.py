def my_func(value):
    return 10
    for i in range(5):
        yield i
    return 10

print(list(my_func(10)))