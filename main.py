from db import init_db
from ui import launch_ui

if __name__ == "_main_":
    print("Initializing database...")
    try:
        init_db()
        print("Database initialized.")
    except Exception as e:
        print(f"Error in init_db(): {e}")

    print("Launching UI...")
    try:
        launch_ui()
    except Exception as e:
        print(f"Error in launch_ui(): {e}")