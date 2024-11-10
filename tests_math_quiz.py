import unittest
from io import StringIO
from unittest.mock import patch

# Assuming the start_quiz function is imported from math_quiz.py
from math_quiz import start_quiz

class TestMathQuiz(unittest.TestCase):

    @patch('builtins.input', return_value='8')  # Mocking user input to simulate correct answer
    @patch('sys.stdout', new_callable=StringIO)  # Capturing the print output
    def test_correct_answer(self, mock_stdout, mock_input):
        start_quiz()
        self.assertIn("Correct!", mock_stdout.getvalue())  # Verifying the output

    @patch('builtins.input', return_value='5')  # Mocking user input to simulate incorrect answer
    @patch('sys.stdout', new_callable=StringIO)  # Capturing the print output
    def test_incorrect_answer(self, mock_stdout, mock_input):
        start_quiz()
        self.assertIn("Incorrect. Try again!", mock_stdout.getvalue())  # Verifying the output

    @patch('builtins.input', return_value='invalid')  # Mocking user input to simulate invalid input
    @patch('sys.stdout', new_callable=StringIO)  # Capturing the print output
    def test_invalid_input(self, mock_stdout, mock_input):
        start_quiz()
        self.assertIn("Please enter a valid number.", mock_stdout.getvalue())  # Verifying the error message

if __name__ == '__main__':
    unittest.main()
