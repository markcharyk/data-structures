import datetime


def make_month(year, month):
    return Month(year, month)


class Month(object):
    def __init__(self, year, month):
        weekday = datetime.date(year, month, 1).weekday()
        self.template = []
        self.month = month
        for date in xrange(7):
            self.template.append((weekday + date) % 7)

    def day(self, date):
        if (
            date > 31 or
            (date > 30 and (self.month == 2 or 4 or 6 or 9 or 11)) or
            (date > 29 and self.month == 2)
        ):
            raise ValueError("day is out of range")
        index = (date - 1) % 7
        weekday = self.template[index]
        # Really really really wanted to use a dict
        if not weekday:
            return 'Mo'
        elif weekday == 1:
            return 'Tu'
        elif weekday == 2:
            return 'We'
        elif weekday == 3:
            return 'Th'
        elif weekday == 4:
            return 'Fr'
        elif weekday == 5:
            return 'Sa'
        return 'Su'
