# Hey, provide me number of days as a comma separated list, I'll convert it to hours!

calculation_to_hours = 24
name_of_unit = 'hours'


def days_to_units (number_of_days):
    return (f"\nGreat, {number_of_days} days are {number_of_days * calculation_to_hours} {name_of_unit}.\n")
    


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)

        # We want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(int(num_of_days_element))
            print(calculated_value)
        elif user_input_number == 0:
            print("\nYou have entered a 0. Kindly input a positive number.\n\n")
        else:
            print("\nYou have enetered a negative number. Just stop doing it!\n\n")
    
    except:
        print("\nYour input isn't a valid number. Don't ruin my program!\n\n")


user_input = ""
while user_input != "exit":
    user_input = input("\nHey, enter a number of days and convestion unit!\n\n")
    #print(type(user_input.split(", ")))
    #print(user_input.split(", "))
    print(type(set(user_input.split(", "))))
    
    for num_of_days_element in set(user_input.split(", ")):
        validate_and_execute()


