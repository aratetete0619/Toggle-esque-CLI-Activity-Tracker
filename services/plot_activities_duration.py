from .db_config import get_connection
import matplotlib.pyplot as plt


def plot_activities_duration():
    cnx = get_connection()
    cursor = cnx.cursor()

    query = """
    SELECT DATE_FORMAT(start_date, '%Y-%m-%d'), SUM(TIME_TO_SEC(duration) / 3600)
    FROM activities
    WHERE duration IS NOT NULL
    GROUP BY DATE_FORMAT(start_date, '%Y-%m-%d')
    ORDER BY DATE_FORMAT(start_date, '%Y-%m-%d');
    """
    cursor.execute(query)
    results = cursor.fetchall()

    dates = [row[0] for row in results]
    durations_in_hours = [row[1] for row in results]

    plt.bar(dates, durations_in_hours, color="blue")
    plt.xlabel("Date")
    plt.ylabel("Total Duration (hours)")
    plt.title("Duration of Activities Per Day")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    cursor.close()
    cnx.close()
