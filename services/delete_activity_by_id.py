from .db_config import get_connection


def delete_activity_by_id(id):
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute("SELECT title FROM activities WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        title = result[0]
        confirm = input(
            f"Are you sure you want to delete activity with ID {id} - {title}? (yes/no): "
        )
        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM activities WHERE id = %s", (id,))
            cnx.commit()
            print(f"Deleted activity with ID {id} - {title}")
        else:
            print("Deletion cancelled")
    else:
        print(f"No activity found with ID {id}")

    cursor.close()
    cnx.close()
