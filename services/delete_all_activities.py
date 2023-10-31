from .db_config import get_connection


def delete_all_activities():
    cnx = get_connection()
    cursor = cnx.cursor()

    confirm = input("Are you sure you want to delete all activities? (yes/no): ")
    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM activities")
        cnx.commit()
        print("Deleted all activities")
    else:
        print("Deletion cancelled")

    cursor.close()
    cnx.close()
