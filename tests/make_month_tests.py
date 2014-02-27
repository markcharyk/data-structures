import unittest
from make_month import make_month
import datetime


class TestMakeMonth(unittest.TestCase):
    def setUp(self):
        self.date_dict = {
            0: 'Mo',
            1: 'Tu',
            2: 'We',
            3: 'Th',
            4: 'Fr',
            5: 'Sa',
            6: 'Su'
        }

    def test_init_bad_month(self):
        with self.assertRaises(ValueError):
            make_month(2013, 13)

    def test_day_today(self):
        month = make_month(2014, 2)
        self.assertEqual(
            month.day(26),
            self.date_dict[datetime.date(2014, 2, 26).weekday()]
        )

    def test_day_last_week(self):
        month = make_month(2014, 2)
        self.assertEqual(
            month.day(19),
            self.date_dict[datetime.date(2014, 2, 19).weekday()]
        )

    def test_day_last_month(self):
        month = make_month(2014, 1)
        self.assertEqual(
            month.day(19),
            self.date_dict[datetime.date(2014, 1, 19).weekday()]
        )

    def test_day_last_year(self):
        month = make_month(2013, 3)
        self.assertEqual(
            month.day(19),
            self.date_dict[datetime.date(2013, 3, 19).weekday()]
        )

    def test_day_past(self):
        month = make_month(1222, 9)
        self.assertEqual(
            month.day(19),
            self.date_dict[datetime.date(1222, 9, 19).weekday()]
        )

    def test_day_future(self):
        month = make_month(2061, 7)
        self.assertEqual(
            month.day(19),
            self.date_dict[datetime.date(2061, 7, 19).weekday()]
        )

    def test_small_year(self):
        month = make_month(56, 1)
        self.assertEqual(
            month.day(26),
            self.date_dict[datetime.date(56, 1, 26).weekday()]
        )

    def test_big_year(self):
        month = make_month(9999, 7)
        self.assertEqual(
            month.day(2),
            self.date_dict[datetime.date(9999, 7, 2).weekday()]
        )

    def test_bad_day(self):
        month = make_month(2014, 11)
        with self.assertRaises(ValueError):
            month = make_month(2014, 11)
            month.day(31)

if __name__ == '__main__':
    unittest.main()
