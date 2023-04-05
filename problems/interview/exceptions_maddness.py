try:
    for i in range(3):
        try:
            1 / 0
        except ZeroDivisionError:
            raise ZeroDivisionError("Divided By Zero")
        finally:
            print("Finally")
            break   # <-- lol
except ZeroDivisionError:
    print("Outer Zero Division")
