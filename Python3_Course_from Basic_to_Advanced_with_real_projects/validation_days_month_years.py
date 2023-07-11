def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True


def days_in_month(year, month):
    month_30 = [4, 6, 9, 11]

    if month == 2:
        if is_year_leap(year) is True:
            return 29
        else:
            return 28
    else:
        if month in month_30:
            return 30
        else:
            return 31


def day_of_year(year, month, day):
    if (year, month, days_in_month(year, month)) == (year, month, day):
        return year, month, day
    else:
        return None


print(day_of_year(2000, 12, 31))
