from .db_config import get_connection
from .utils.datetime_input import datetime_input
from .utils.calculate_duration import calculate_duration


def edit_activity(id):
    cnx = get_connection()
    cursor = cnx.cursor()

    query = "SELECT title, start_date, start_time, end_date, end_time FROM activities WHERE id = %s"
    cursor.execute(query, (id,))
    title, start_date, start_time, end_date, end_time = cursor.fetchone()

    new_title = input(f"Enter new title (current: {title}, or leave blank): ") or title

    start_date, start_time = datetime_input(start_date, start_time, "Start")

    if end_date and end_time:
        end_date, end_time = datetime_input(end_date, end_time, "End")
    else:
        end_date, end_time = None, None

    duration = calculate_duration(start_date, start_time, end_date, end_time)

    update_activity = "UPDATE activities SET title = %s, start_date = %s, start_time = %s, end_date = %s, end_time = %s, duration = %s WHERE id = %s"
    cursor.execute(
        update_activity,
        (new_title, start_date, start_time, end_date, end_time, duration, id),
    )

    cnx.commit()
    cursor.close()
    cnx.close()

    print(f"Updated activity with ID {id}")
