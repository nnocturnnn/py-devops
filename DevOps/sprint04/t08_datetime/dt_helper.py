import datetime
import pytz

def create_datetime(*args, timezone_str=None):
    if timezone_str:
        return pytz.timezone(timezone_str).localize(datetime.datetime(*args))
    else:
        return datetime.datetime(*args)

def print_formatted_datetime(dt_obj, format_t):
    print(dt_obj.strftime(format_t))

def print_difference(dt_obj, s_dt_obj, timezone_str=None):
    if timezone_str:
        tim = pytz.timezone(timezone_str)
        print(dt_obj.replace(tzinfo=tim) - s_dt_obj.replace(tzinfo=tim))
    else:
        print(dt_obj.replace(tzinfo=timezone_str) - s_dt_obj.replace(tzinfo=timezone_str))
    