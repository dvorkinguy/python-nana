calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units(number_of_days):
    return f"\nGreat, {number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}.\n"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            # Corrected this line to use the correct variable 'num_of_days_element'
            calculated_value = days_to_units(int(num_of_days_element))
            print(calculated_value)
        elif user_input_number == 0:
            print("\nYou have entered 0. Kindly input a positive number.\n\n")
        else:
            print("\nYou have entered a negative number. Just stop doing it!\n\n")
    
    except:
        print("\nYour input isn't a valid number. Don't ruin my program!\n\n")

user_input = ""
while user_input != "exit":
    user_input = input("\nHey, provide me with some number!\n")
    for num_of_days_element in user_input.split():
        # Updated the function call to pass the correct variable 'num_of_days_element'
        validate_and_execute()
