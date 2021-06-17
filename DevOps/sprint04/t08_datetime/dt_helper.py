import datetime
import pytz

def create_datetime(*args, timezone_str=None):
    return pytz.timezone(timezone_str).localize(datetime.datetime(*args))

def print_formatted_datetime(dt_obj, format_t):
    print(dt_obj.strftime(format_t))

def print_difference(dt_obj, s_dt_obj, timezone_str=None):
    if timezone_str:
        print(pytz.timezone(timezone_str).localize(dt_obj) - pytz.timezone(timezone_str).localize(s_dt_obj))
    else:
        print(dt_obj - s_dt_obj)
