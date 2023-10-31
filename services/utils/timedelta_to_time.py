import datetime


def timedelta_to_time(delta):
    return (datetime.datetime.min + delta).time()
