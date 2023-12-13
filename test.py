
calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units (number_of_days):
    return (f"Great, {number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}.")


user_input = input("hey, provide me some number!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)

