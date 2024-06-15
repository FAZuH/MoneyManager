import unittest
from unittest.mock import MagicMock, patch

from moneymanager import display


class TestDisplay(unittest.TestCase):

    @patch('builtins.exit')
    @patch('builtins.input', side_effect=["bye", "exit"])
    def test_ask(self, mock_input: MagicMock, mock_exit: MagicMock) -> None:
        # Test if return value of input() is returned
        inpt1 = display.exittable_input('')
        self.assertEqual(inpt1, "bye")

        # Test if exit() is called if user inputs 'exit'
        display.exittable_input('')
        mock_exit.assert_called_once()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["1", "abcdef", "2"])
    def test_must_get_input(self, mock_input: MagicMock, mock_print: MagicMock) -> None:
        # Test if must_get_input() returns valid parsed input
        inpt1 = display.must_get_input('', int)
        self.assertEqual(inpt1, 1)

        # Test if must_get_input() prints error message if invalid input,
        # Then prompts the user again and returns valid parsed input
        inpt2 = display.must_get_input('', int)
        mock_print.assert_called_with("Please enter a valid input.")
        self.assertEqual(inpt2, 2)

    @unittest.skip("Not important")
    def test_display_welcome(self) -> None: ...

    @unittest.skip("Functions used are ")
    def test_prompt_main(self) -> None: ...
