# add import

from question_a import get_bonus_pay_amount

while True:
    try:
        sales_input = input("Enter sales amount (or 'quit' to exit): ")
        if sales_input.lower() == 'quit':
            break
        sales_amount = float(sales_input)
        bonus = get_bonus_pay_amount(sales_amount)
        print(bonus)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'quit'.")
