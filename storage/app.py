from flask import Flask, request, Response
import pathlib, os

def startup_tasks():
    """
    Needed tasks to check if data directory exists and inside 
    is a app.log file. Creates new directory and file if the
    file and dir don't exist
    """
    global log_file
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

@app.route('/log', methods=['POST'])
def inject_log():

    if(request.content_type != 'text/plain'):
        return Response("Content-Type must be text/plain", status=415)

    data = request.args.get("timestamp")
    data = data.rstrip()
    if(len(data) == 0):
        return Response("Timestamp value is empty", status=400)
    
    with (log_file, 'a') as file:
        file.write(f"{data}\n")
    return Response("Log updated", status=204)

@app.route('/log', methods=['GET'])
def read_log():
    try:
        with open(log_file, 'r') as file:
            content = file.read()
        return Response(content,
                        mimetype='text/plain',
                        status=200)
    except FileNotFoundError:
        return Response("Log file not found", status=404)
    except Exception  as e:
        return Response(f"Error reading the file: {e}", status=500)
        