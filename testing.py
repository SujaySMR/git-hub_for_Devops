import unittest


def add_numbers(first: int, second: int) -> int:
    return first + second


class AddNumbersTests(unittest.TestCase):
    def test_adds_positive_numbers(self) -> None:
        self.assertEqual(add_numbers(2, 3), 5)

    def test_adds_negative_numbers(self) -> None:
        self.assertEqual(add_numbers(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
