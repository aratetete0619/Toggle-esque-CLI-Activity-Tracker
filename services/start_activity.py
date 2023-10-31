import datetime
from .db_config import get_connection


def start_activity(title):
    cnx = get_connection()
    cursor = cnx.cursor()

    start_date = datetime.datetime.now().date()
    start_time = datetime.datetime.now().time()
    add_activity = (
        "INSERT INTO activities (title, start_date, start_time) VALUES (%s, %s, %s)"
    )
    cursor.execute(add_activity, (title, start_date, start_time))

    cnx.commit()
    cursor.close()
    cnx.close()
    print(f"Started {title} at {start_date} {start_time}")
