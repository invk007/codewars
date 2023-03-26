my_list = list(range(1, 7))
enum = enumerate(my_list)
my_list.pop(-1)
my_list.pop(2)
my_list.pop(3)
for index, item in enum:
    print(f"{index=}")
    print(index, item)

print(my_list)