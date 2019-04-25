#!/usr/bin/env python3

import subprocess
import webbrowser

bash = "pipenv run python3 mysite/manage.py runserver"
process = subprocess.Popen(bash.split(), stdout=subprocess.PIPE)
webbrowser.open("http://127.0.0.1:8000/webapp/home", new = 1)
output, error = process.communicate()
