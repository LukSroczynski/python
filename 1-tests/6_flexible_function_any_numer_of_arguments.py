def flexible_number_of_arguments(*args):
    for i in args:
        print(i)


def flexible_number_of_arguments_total(*args):
    total = 0
    for i in args:
        total += i
    return total


flexible_number_of_arguments(1, 2, 3, 4, "Hello There!")

print(flexible_number_of_arguments_total(1, 2, 7, 4, 1, 4, 6))
