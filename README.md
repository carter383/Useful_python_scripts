Useful Python Scripts

    time_date_util.py:

        get_now:
        returns current time date as datetime
        
        get_date:
        returns date as text format 'DD:MM:YYYY'

        get_time:
        returns time as text format 'HH:MM:SS'

        get_day(date as datetime (default = now)):
        returns day as text format 'DD'

        get_month(date as datetime (default = now)):
        returns month as text format 'MM'

        get_year(date as datetime (default = now)):
        returns year as text format 'YYYY'

        get_hour(time(default = now)):
        returns hour as text format 'HH'

        get_minute(time(default = now)):
        returns minute as text format 'MM'
        
        get_second(time(default = now)):
        returns second as text format 'SS'

        get_weekday(date as datetime (default = now)):
        returns weekday as text example 'Monday'

        get_weeknum(date as datetime (default = now)):
        returns weeknumber as int

        get_month_name(date as datetime (default = now)):
        returns month as text example 'January'

        add_years(years_to_add, date as datetime (default = now)):
        returns date add years to add as text format 'DD:MM:YYYY'

        add_months(months_to_add, date as datetime (default = now)):
        returns  date add months to add as text format 'DD:MM:YYYY'

        add_days(days_to_add, date as datetime (default = now)):
        returns date add days to add as text format 'DD:MM:YYYY'

        add_hours(hours_to_add, time as datetime (default = now)):
        returns time add hours to add as text format 'HH:MM:SS'

        add_minutes(minutes_to_add, time as datetime (default = now)):
        returns time add minutes to add as text format 'HH:MM:SS'

        add_seconds(seconds_to_add, time as datetime (default = now)):
        returns time add seconds to add as text format 'HH:MM:SS'