import datetime

user_input = input("Eneter your Goal and Time sepateted by colon(:)\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(f"Dear user! Time remaining to your goal is: {goal} is {int(time_till.total_seconds() / 60 / 60)} hours")