import jdatetime

import sys
import argparse
import textwrap

try:
    from wodev.wodev import Wodev
except ImportError:
    from wodev import Wodev


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
