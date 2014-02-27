import calendar


def make_month(year, month):
    return Month(year, month)


class Month(object):
    def __init__(self, year, month):
        self.template = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        weekday, self.last = calendar.monthrange(year, month)
        self.template = self.template[weekday - 1::] + self.template[:weekday - 1:]

    def day(self, date):
        if date > self.last:
            raise ValueError("day is out of range")
        index = date % 7
        return self.template[index]
