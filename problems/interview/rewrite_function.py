def type_checker(variable):
    if isinstance(variable, (float, int)):
        print(f"{variable} is a number")
    elif isinstance(variable, str):
        print(f"{variable} is a string")
    else:
        print(f"{variable} is something else")


if __name__ == "__main__":
    type_checker(variable="Python")