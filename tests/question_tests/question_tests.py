import unittest
from question_a.question_a import test_get_bonus_pay_amount
from question_b.question_b import use_local_variable
from question_c.question_c import reverse_string
from question_d.question_d import get_day_of_week

class TestQuestions(unittest.TestCase):

    # Question A
    def test_question_a_config(self):
        self.assertEqual(True, test_get_bonus_pay_amount())

    # Question B
    def test_local_variable_scope(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)

    # Question C
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")

    # Question D
    def test_day_of_week(self):
        self.assertEqual(get_day_of_week(0), "Invalid number")
        self.assertEqual(get_day_of_week(1), "Monday")
        self.assertEqual(get_day_of_week(2), "Tuesday")
        self.assertEqual(get_day_of_week(3), "Wednesday")
        self.assertEqual(get_day_of_week(4), "Thursday")
        self.assertEqual(get_day_of_week(5), "Friday")
        self.assertEqual(get_day_of_week(6), "Saturday")