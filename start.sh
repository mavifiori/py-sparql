source venv/bin/activate
python -m flask run &
sleep 1 && xdg-open http://localhost:5000
