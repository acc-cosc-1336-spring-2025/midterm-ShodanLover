#add import

from question_d import get_day_of_week

while True:
    user_input = input("Enter a number (1-7) or 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break
    try:
        day_number = int(user_input)
        result = get_day_of_week(day_number)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")