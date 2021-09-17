import jdatetime

import sys
import os
import logging
import argparse
import textwrap


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


def set_log_handler(log_path='logs/', log_file='file'):
    if not os.path.isdir(log_path):
        os.makedirs(log_path)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s: "%(message)s"')
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("{0}/{1}.log".format(log_path, log_file))
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    return root_logger


def main():
    parser = argparse.ArgumentParser(
        description="""WOdEv: Week Odd (or) Even""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """developed by Mohammad Salek"""
        ),
        prog='wodev',
    )
    parser.add_argument('--show-first-week', help='show the starting/first week.', action='store_true')
    parser.add_argument('--change-first-week', type=str, help='change the starting/first week.')
    try:
        args = vars(parser.parse_args())
        if args['show_first_week']:
            wodev = Wodev()
            msg = "first week: {}".format(str(wodev.first_week))
            print(msg)
        elif args['change_first_week']:
            input_date = args['change_first_week']
            if input_date.count('-') != 2:
                raise Exception("Please provide a correct date format: xxxx-xx-xx (year-month-day)")
            try:
                year, month, day = [int(x) for x in input_date.split("-")]
                new_first_week = jdatetime.date(year, month, day)
            except Exception as err:
                logging.error("Error converting input date:")
                raise err
            wodev = Wodev(first_week=new_first_week)
            print(wodev.odev_msg())
        else:
            wodev = Wodev()
            print(wodev.odev_msg())
    except argparse.ArgumentTypeError as arg_err:
        print('\n\nan argument error occurred:', arg_err)
        print('wodev -h for help')
        sys.exit(1)


if __name__ == "__main__":
    main()
