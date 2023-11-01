import datetime
from .db_config import get_connection
import pytz


def start_activity(title, timezone_str="Asia/Tokyo"):
    cnx = get_connection()
    cursor = cnx.cursor()

    local_timezone = pytz.timezone(timezone_str)
    local_dt = datetime.datetime.now(local_timezone)
    start_date = local_dt.date()
    start_time = local_dt.time()

    add_activity = (
        "INSERT INTO activities (title, start_date, start_time) VALUES (%s, %s, %s)"
    )
    cursor.execute(add_activity, (title, start_date, start_time))

    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Started {title} at {start_date} {start_time}")
