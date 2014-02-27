import calendar


def make_month(year, month):
    return Month(year, month)


class Month(object):
    def __init__(self, year, month):
        alphas, self.template = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'], []
        weekday, self.last = calendar.monthrange(year, month)
        for date in xrange(7):
            self.template.append(alphas[(weekday + date - 1) % 7])

    def day(self, date):
        if date > self.last:
            raise ValueError("day is out of range")
        index = date % 7
        return self.template[index]
