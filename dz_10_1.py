import calendar
import sys

month_str = [calendar.month_name[i] for i in range(1, 13)]


def month_name():
    try:
        month_num = int(input("please enter the number of the month: ")) - 1
        if month_num < 0:
            raise Exception(f'month can be in range from 1 to 12. please proceed accordingly')
        return month_str[month_num]
    except IndexError as ex1:
        print(f'month can be in range from 1 to 12. please proceed accordingly {ex1}')
    except ValueError as ex3:
        print(f'please enter the number not the text')
    finally:
        print(f'successfully done!')

print(month_name())

