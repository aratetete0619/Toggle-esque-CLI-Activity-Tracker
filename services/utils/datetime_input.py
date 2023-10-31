import datetime


def convert_timedelta_to_time(delta):
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return datetime.time(hour=hours, minute=minutes)


def datetime_input(current_date, current_time, prefix):
    if isinstance(current_time, datetime.timedelta):
        current_time = convert_timedelta_to_time(current_time)

    print(f"--- Editing {prefix} Date & Time ---")
    print(f"Current {prefix} Date: {current_date.strftime('%Y-%m-%d')}")
    print(f"Current {prefix} Time: {current_time.strftime('%H:%M')}")

    year = int(
        input(f"{prefix} Year (e.g., YYYY, default: {current_date.year}): ")
        or current_date.year
    )
    month = int(
        input(f"{prefix} Month (e.g., MM, default: {current_date.month}): ")
        or current_date.month
    )
    day = int(
        input(f"{prefix} Day (e.g., DD, default: {current_date.day}): ")
        or current_date.day
    )
    hour = int(
        input(f"{prefix} Hour (e.g., HH, default: {current_time.hour}): ")
        or current_time.hour
    )
    minute = int(
        input(f"{prefix} Minute (e.g., MM, default: {current_time.minute}): ")
        or current_time.minute
    )

    print("------------------------------")

    return datetime.date(year, month, day), datetime.time(hour, minute)
