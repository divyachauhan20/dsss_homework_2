# This function starts the math quiz and asks the user a math question.
def start_quiz():
    """
    Starts a simple math quiz asking the user 'What is 5 + 3?'.

    The function checks if the user enters the correct answer, 8.
    If the answer is wrong, it prompts the user to try again.
    """
    try:
        # Ask the user to solve a simple math problem
        user_input = int(input("What is 5 + 3? "))

        # Check if the user entered the correct answer
        if user_input == 8:
            print("Correct!")
        else:
            print("Incorrect. Try again!")
    except ValueError:
        # Handle the case where the user enters something that's not a number
        print("Please enter a valid number.")