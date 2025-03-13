#add import

from question_c import reverse_string

while True:
    user_string = input("Enter a string (or 'quit' to exit): ")
    if user_string.lower() == 'quit':
        break
    reversed_result = reverse_string(user_string)
    print(f"Reversed string: {reversed_result}")