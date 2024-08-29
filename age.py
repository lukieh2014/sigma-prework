from datetime import datetime, timedelta  # importing useful modules

input_date = input("Please enter the start date here (DD-MM-YYYY): ")
# converting user-inputted date into datetime object
input_date = datetime.strptime(input_date, "%d-%m-%Y")
print(input_date)

current_date = datetime.today()  # setting current date as today's date
print(current_date)

age = current_date.year - input_date.year

if (current_date.month, current_date.day) < (input_date.month, input_date.day):
    # adjusts age to account for current date (day, month) being before the date (day, month) of the inputted date in the inputted year
    age -= 1

print(age)
