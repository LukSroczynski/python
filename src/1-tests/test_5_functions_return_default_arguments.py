def print_hello_world():
    print("Hello World!")


def btc_to_usd(btc):
    amount = btc * 527
    return amount


def print_age_range(age_from=1, age_to=20):
    limit_age = []
    for i in range(age_from, age_to):
        limit_age.append(i/2 + 7)
    return limit_age


# print_hello_world()
#
# print(btc_to_usd(1.15))
# print(btc_to_usd(1.23))
#
# print(print_age_range())  # Default arguments
# print(print_age_range(age_to=30))

