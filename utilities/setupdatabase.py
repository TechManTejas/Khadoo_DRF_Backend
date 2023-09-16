import subprocess
from khadoo_drf_backend.settings import PROJECT_APPS

def setupdatabase():
    for app in PROJECT_APPS:
        # Run makemigrations for the app
        subprocess.run(['python', 'manage.py', 'makemigrations', app])

        # Run migrate for the app
        subprocess.run(['python', 'manage.py', 'migrate', app])

    # Run general migrations
    subprocess.run(['python', 'manage.py', 'makemigrations'])
    subprocess.run(['python', 'manage.py', 'migrate'])

    # Create a superuser with username 'SUPERUSER' and password 'SUPERUSER'
    subprocess.run(['python', 'manage.py', 'createsuperuser', '--username=SUPERUSER', '--email=', '--verbosity=0'])
    print("Superuser 'SUPERUSER' with password 'SUPERUSER' created.")

