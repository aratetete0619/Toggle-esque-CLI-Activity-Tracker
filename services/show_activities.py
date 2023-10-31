import datetime
from .db_config import get_connection
from .utils.timedelta_to_time import timedelta_to_time


def show_activities():
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "SELECT id, title, start_date, start_time, end_date, end_time FROM activities ORDER BY start_date DESC, start_time DESC"
    cursor.execute(query)

    print("ID | Title | Start Date | Start Time | End Date | End Time | Duration")
    print("----------------------------------------------------------------------")
    for id, title, start_date, start_time, end_date, end_time in cursor:
        if end_date and end_time:
            start_datetime = datetime.datetime.combine(
                start_date, timedelta_to_time(start_time)
            )
            end_datetime = datetime.datetime.combine(
                end_date, timedelta_to_time(end_time)
            )
            duration = end_datetime - start_datetime
            duration_str = str(duration)
        else:
            duration_str = "Ongoing"

        print(
            f"{id} | {title} | {start_date} {start_time} | {end_date} {end_time} | {duration_str}"
        )

    cursor.close()
    cnx.close()
