# coding=utf-8
from dateutil.parser import parse as parse_datetime

type_to_class = {}


def entity_type_name_to_class(type_name):
    return type_to_class[type_name.lower()]


def format_date(date, precision):
    if date is None:
        return None

    if precision == 'YEAR':
        return '{:02}'.format(date.year)
    elif precision == 'MONTH':
        return '{:02}-{:02}'.format(date.year, date.month)
    else:
        return '{:02}-{:02}-{:02}'.format(date.year, date.month, date.day)


def parse_date(date):
    if date:
        return parse_datetime(date).date()
    else:
        return None
