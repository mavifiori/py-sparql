source venv/bin/activate
python -m flask run &
sleep 2 && xdg-open http://localhost:5000
