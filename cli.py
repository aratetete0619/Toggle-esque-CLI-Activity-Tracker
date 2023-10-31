from services.start_activity import start_activity
from services.end_activity import end_activity
from services.edit_activity import edit_activity
from services.export_csv import export_csv
from services.show_activities import show_activities
from services.delete_activity_by_id import delete_activity_by_id
from services.delete_all_activities import delete_all_activities
from services.create_activity import create_activity
from services.plot_activities_duration import plot_activities_duration


while True:
    command = input(
        "Enter command (start/end/create/edit/export/show/delete_id/delete_all/stats/quit): "
    )
    if command == "start":
        title = input("Enter activity title: ")
        start_activity(title)
    elif command == "end":
        id = int(input("Enter activity ID to end: "))
        end_activity(id)
    elif command == "edit":
        id = int(input("Enter activity ID to edit: "))
        edit_activity(id)
    elif command == "export":
        year = input("Enter year: ")
        month = input("Enter month: ")
        export_csv(year, month)
    elif command == "show":
        show_activities()
    elif command == "delete_id":
        id = int(input("Enter activity ID to delete: "))
        delete_activity_by_id(id)
    elif command == "delete_all":
        delete_all_activities()
    elif command == "create":
        create_activity()
    elif command == "stats":
        plot_activities_duration()
    elif command == "quit":
        break
    else:
        print("Invalid command")
