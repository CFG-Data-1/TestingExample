import unittest

from shop import *


class WelcomeTest(unittest.TestCase):
    def test_welcome(self):
        self.assertEqual(welcome(), "Welcome to the fruit shop!")


class ExitShoppingTest(unittest.TestCase):
    def test_exit(self):
        with self.assertRaises(SystemExit):
            exit_shopping()


class CheckFundsTest(unittest.TestCase):
    def test_check_funds(self):
        response = check_funds(50, "bananas")
        self.assertTrue(response)

    def test_check_neg_funds(self):
        response = check_funds(10, "oranges")
        self.assertEqual(response, False)


class BeginShoppingTest(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(
            begin_shopping("apples", 100, 1),
            "Here’s your apples! and you are left with 50"
        )

    def test_invalid_input(self):
        with self.assertRaises(SystemExit):
            begin_shopping("e", 100, 1)

    def test_max_tries_exception(self):
        with self.assertRaises(ExceededMaxCountException):
            begin_shopping("apples", 100, 5)

    def test_invalid_amount(self):
        with self.assertRaises(InvalidInputException):
            begin_shopping("apples", -1, 0)

    def test_invalid_input_amount(self):
        with self.assertRaises(TypeError):
            begin_shopping("apples", "d", 0)


if __name__ == '__main__':
    unittest.main()
