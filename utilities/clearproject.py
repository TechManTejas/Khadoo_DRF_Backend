import os
import shutil
from khadoo_drf_backend.settings import PROJECT_APPS

def clear_app_data(app_name):
    # Delete migrations folder
    migrations_path = os.path.join(app_name, 'migrations')
    if os.path.exists(migrations_path):
        shutil.rmtree(migrations_path)
        print(f"Deleted migrations folder for {app_name}")

    # Delete __pycache__ folder
    pycache_path = os.path.join(app_name, '__pycache__')
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
        print(f"Deleted __pycache__ folder for {app_name}")

def clearproject():
    for app_name in PROJECT_APPS:
        clear_app_data(app_name)

    # Delete db.sqlite3 file
    if os.path.exists('db.sqlite3'):
        os.remove('db.sqlite3')
        print("Deleted db.sqlite3 file")

if __name__ == "__main__":
    print("Starting cleanup...")
    clearproject()
    print("Cleanup completed.")
