from flask import Flask
import os, pathlib

def startup_tasks():
    """
    Needed tasks to check if data directory exists and inside 
    is a app.log file. Creates new directory and file if the
    file and dir don't exist
    """
    data_dir = pathlib.Path(os.getenv("DATA_DIR", "/data"))
    log_file = data_dir / "app.log"
    data_dir.mkdir(parents=True, exist_ok=True)
    log_file.parent.mkdir(parents=True, exist_ok=True) 
    log_file.touch(exist_ok=True)

def create_app():
    """
    Creates the flask applicaiton.
    """
    app = Flask(__name__)
    startup_tasks()
    return app

app = create_app()