import subprocess

subprocess.run("pipenv run python3 mysite/manage.py runserver", shell=True, check=True)
