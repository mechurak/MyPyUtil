"""
Weekly 투두 template generator
"""

import argparse
import datetime


def print_template(start_date: str):
    date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    for i in range(7):
        cur_date = date + datetime.timedelta(days=i)
        print(cur_date.strftime('## %Y-%m-%d (%a)'))
        print('- [ ] temp\n\n')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--start", required=True, help="start date (ex. 2022-07-17)")
    args = vars(ap.parse_args())

    print_template(args['start'])
