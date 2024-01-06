.venv\Scripts\activate
start /B python -m flask run
timeout /t 2
start http://localhost:5000