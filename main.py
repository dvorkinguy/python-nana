
calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units (number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}.")


my_var = days_to_units(20)

user_input = input("Hey user, input days, and i will convert it to hours!\n")
print(user_input)