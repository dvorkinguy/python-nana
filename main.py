
calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units (number_of_days):
    conditional_check = number_of_days > 0
    print(type(conditional_check))

    if number_of_days > 0:
        return (f"\nGreat, {number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}.\n")
    elif number_of_days == 0:
        return (f"\nYou have entered a 0. Kindly input a positive number.\n")
    else:
        return "\nYou have entered a negative value. Unble to calculate.\n"


user_input = input("\nHey, provide me with some number!\n\n")
user_input_number = int(user_input)

calculated_value = days_to_units(int(user_input))
print(calculated_value)

