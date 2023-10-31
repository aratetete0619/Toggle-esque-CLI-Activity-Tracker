import csv
import os
import datetime
from .db_config import get_connection
from .utils.timedelta_to_time import timedelta_to_time


def export_csv(year, month):
    cnx = get_connection()
    cursor = cnx.cursor()

    query = f"SELECT title, start_date, start_time, end_date, end_time FROM activities WHERE YEAR(start_date) = {year} AND MONTH(start_date) = {month}"
    cursor.execute(query)

    directory_path = os.path.join(os.getcwd(), "csv")
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    filename = f"{directory_path}/activity_log_{year}_{month}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = [
            "title",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "duration",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for title, start_date, start_time, end_date, end_time in cursor:
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

            writer.writerow(
                {
                    "title": title,
                    "start_date": start_date,
                    "start_time": timedelta_to_time(start_time),
                    "end_date": end_date if end_date else "",
                    "end_time": timedelta_to_time(end_time) if end_time else "",
                    "duration": duration_str,
                }
            )
    print(f"Exported to {filename}")
    cursor.close()
    cnx.close()
