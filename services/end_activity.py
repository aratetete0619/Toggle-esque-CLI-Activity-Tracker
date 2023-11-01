import datetime
import os
import pytz
from .db_config import get_connection
from .utils.timedelta_to_time import timedelta_to_time
from dotenv import load_dotenv

load_dotenv()


def end_activity(id):
    timezone_str = os.environ.get("USER_TIMEZONE", "Asia/Tokyo")
    local_timezone = pytz.timezone(timezone_str)

    local_datetime = datetime.datetime.now(local_timezone)
    end_date = local_datetime.date()
    end_time = local_datetime.time()

    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("SELECT start_time FROM activities WHERE id = %s", (id,))
    start_time = cursor.fetchone()[0]

    start_time = timedelta_to_time(start_time)

    if not start_time:
        print("Error: Start time not found for ID:", id)
        return

    start_datetime = datetime.datetime.combine(local_datetime.date(), start_time)
    end_datetime = datetime.datetime.combine(local_datetime.date(), end_time)

    duration = end_datetime - start_datetime

    update_activity = "UPDATE activities SET end_date = %s, end_time = %s, duration = %s WHERE id = %s"
    cursor.execute(update_activity, (end_date, end_time, duration, id))

    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Ended activity with ID {id} at {end_date} {end_time}")
