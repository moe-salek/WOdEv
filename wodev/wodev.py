import jdatetime


class Wodev:
    def __init__(self, is_shamsi=True, first_week=None):
        self.is_shamsi = is_shamsi
        self.today = jdatetime.date.today()
        if first_week:
            self.first_week = first_week
        else:
            if is_shamsi:
                self.first_week = jdatetime.date(1400, 6, 22)
            else:
                self.first_week = jdatetime.date(1400, 6, 22).togregorian()

    def compute_days_passed(self) -> int:
        return (jdatetime.date.today() - self.first_week).days

    def odev(self) -> str:
        """returns 'odd' or 'even'.
        """
        days_passed = self.compute_days_passed()
        if days_passed >= 0:
            is_odd = (days_passed // 7) % 2 == 0
            return "odd" if is_odd else "even"
        else:
            raise ValueError("first week hasn't reached yet!")

    def odev_msg(self) -> str:
        msg = "first week: {},\ntoday: {},\nodev: {}".format(
            str(self.first_week),
            str(self.today),
            self.odev().upper()
        )
        return msg
