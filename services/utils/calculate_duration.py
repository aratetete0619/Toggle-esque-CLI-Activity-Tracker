import datetime


def calculate_duration(start_date, start_time, end_date, end_time):
    if all([start_date, start_time, end_date, end_time]):
        start_datetime = datetime.datetime.combine(start_date, start_time)
        end_datetime = datetime.datetime.combine(end_date, end_time)
        duration_timedelta = end_datetime - start_datetime
        return duration_timedelta
    return None
