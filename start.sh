source venv/bin/activate
gunicorn --workers 2 --bind unix:mydiskotek.sock -m 007 myapp:app
deactivate
