import datetime
from .db_config import get_connection
from .utils.datetime_input import datetime_input
from .utils.calculate_duration import calculate_duration


def create_activity():
    cnx = get_connection()
    cursor = cnx.cursor()

    # Input title for the new activity
    title = input("Enter title for the new activity: ")

    # Use today's date and current time as default for new activity
    default_date = datetime.date.today()
    default_time = datetime.datetime.now().time()

    # Get date and time inputs for the new activity
    start_date, start_time = datetime_input(default_date, default_time, "Start")

    # Ask the user if they want to add an end time for the activity
    has_end_time = input(
        "Do you want to add an end date and time? (yes or no): "
    ).lower()
    if has_end_time == "yes":
        end_date, end_time = datetime_input(default_date, default_time, "End")
    else:
        end_date, end_time = None, None

    duration = calculate_duration(start_date, start_time, end_date, end_time)

    # Insert the new activity into the database
    insert_activity = "INSERT INTO activities (title, start_date, start_time, end_date, end_time, duration) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(
        insert_activity, (title, start_date, start_time, end_date, end_time, duration)
    )

    cnx.commit()
    cursor.close()
    cnx.close()

    print("New activity created!")
