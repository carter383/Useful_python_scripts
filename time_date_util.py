from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


def get_now():
    now = datetime.now()
    return now
def get_date():
    now = get_now()
    date = now.strftime('%d/%m/%Y')
    return date
def get_time():
    now = get_now()
    time = now.strftime('%H/%M:%S')
    return time


def get_timestamp(time:datetime = None):
    if time is None:
        time = get_now()
    timestamp = datetime.timestamp(time)
    return timestamp

def get_day(date:datetime = None):
    if date is None:
        date = get_now()
    day = date.strftime('%d')
    return day
def get_month(date:datetime = None):
    if date is None:
        date = get_now()
    month = date.strftime('%m')
    return month
def get_year(date:datetime = None):
    if date is None:
        date = get_now()
    year = date.strftime('%Y')
    return year


def get_hour(time:datetime = None):
    if time is None:
        time = get_now()
    hour = time.strftime('%H')
    return hour
def get_minute(time:datetime = None):
    if time is None:
        time = get_now()
    minute = time.strftime('%M')
    return minute
def get_second(time:datetime = None):
    if time is None:
        time = get_now()
    second = time.strftime('%S')
    return second

def get_weekday(date:datetime = None):
    if date is None:
        date = get_now()
    weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return weekday[datetime.weekday(date)]

def get_month_name(date:datetime = None):
    if date is None:
        date = get_now()
    months = ['January','Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month  = int(get_month(date)) - 1
    return months[month]

def get_weeknum(date:datetime = None):
    if date is None:
        date = get_now()
    weeknum = date.isocalendar()[1]
    return int(weeknum)

def add_years(years_to_add, date:datetime = None):
    if date is None:
        date = get_now()
    newdate = date + relativedelta(years=years_to_add)
    textdate = newdate.strftime('%d/%m/%Y')
    return textdate, newdate

def add_months(months_to_add, date:datetime = None):
    if date is None:
        date = get_now()
    if months_to_add > 12:
        years = int(months_to_add/12)
        months_to_add = months_to_add % 12
        add_years(years,date)
    newdate = date + relativedelta(months=months_to_add)
    textdate = newdate.strftime('%d/%m/%Y')
    return textdate, newdate

def add_days(days_to_add, date:datetime = None):
    if date is None:
        date = get_now()
    newdate = date + relativedelta(days=days_to_add)
    textdate = newdate.strftime('%d/%m/%Y')
    return textdate, newdate


def add_hours(hours_to_add, time:datetime = None):
    if time is None:
        time = get_now()
    newtime = time + timedelta(hours=hours_to_add)
    texttime =newtime.strftime('%H/%M:%S')
    return texttime, newtime

def add_minutes(minutes_to_add, time:datetime = None):
    if time is None:
        time = get_now()
    if minutes_to_add > 60:
        hours =  int(minutes_to_add/60)
        minutes_to_add = minutes_to_add %60
        add_hours(hours)
    newtime = time + timedelta(minutes=minutes_to_add)
    texttime =newtime.strftime('%H/%M:%S')
    return texttime, newtime

def add_seconds(seconds_to_add, time:datetime = None):
    if time is None:
        time = get_now()
    if seconds_to_add > 60:
        minutes =  int(seconds_to_add/60)
        seconds_to_add = seconds_to_add %60
        add_minutes(minutes)
    newtime = time + timedelta(seconds=seconds_to_add)
    texttime =newtime.strftime('%H/%M:%S')
    return texttime, newtime
