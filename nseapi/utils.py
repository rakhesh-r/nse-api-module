import datetime

_DATE_FORMAT = "%d-%m-%Y"


# from_date should be less than to_date
# format DD-MM-YYYY
def get_difference_dates(from_date: str, to_date: str) -> int:
    d1 = datetime.datetime.strptime(from_date, _DATE_FORMAT).date()
    d2 = datetime.datetime.strptime(to_date, _DATE_FORMAT).date()
    delta = d2 - d1
    if delta.days < 0:
        raise Exception("from_date should be less than to_date")
    return delta.days


def get_date_after_n_days(from_date, n_days):
    if not from_date:
        d1 = datetime.date.today()
    else:
        d1 = datetime.datetime.strptime(from_date, _DATE_FORMAT).date()
    d2 = d1 + datetime.timedelta(days=n_days)
    return d2.strftime(_DATE_FORMAT)


def get_date_before_n_days(to_date, n_days):
    if not to_date:
        d1 = datetime.date.today()
    else:
        d1 = datetime.datetime.strptime(to_date, _DATE_FORMAT).date()
    d2 = d1 - datetime.timedelta(days=n_days)
    return d2.strftime(_DATE_FORMAT)


def get_today_date():
    return datetime.date.today().strftime(_DATE_FORMAT)

# print(get_date_after_n_days(None, 1))
# print(get_difference_dates('01-07-2020', '13-07-2020'))
