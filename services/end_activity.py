import datetime
from .db_config import get_connection
from .utils.timedelta_to_time import timedelta_to_time


def end_activity(id):
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("SELECT start_time FROM activities WHERE id = %s", (id,))
    start_time = cursor.fetchone()[0]

    start_time = timedelta_to_time(start_time)

    if not start_time:
        print("Error: Start time not found for ID:", id)
        return

    end_date = datetime.datetime.now().date()
    end_time = datetime.datetime.now().time()

    start_datetime = datetime.datetime.combine(
        datetime.datetime.now().date(), start_time
    )
    end_datetime = datetime.datetime.combine(datetime.datetime.now().date(), end_time)

    duration = end_datetime - start_datetime

    update_activity = "UPDATE activities SET end_date = %s, end_time = %s, duration = %s WHERE id = %s"
    cursor.execute(update_activity, (end_date, end_time, duration, id))

    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Ended activity with ID {id} at {end_date} {end_time}")
