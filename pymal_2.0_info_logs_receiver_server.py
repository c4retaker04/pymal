from flask import Flask, request
from pathlib import Path

app = Flask(__name__)
UPLOAD_FOLDER = Path("uploaded")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    UPLOAD_FOLDER.mkdir(exist_ok=True)
    save_path = UPLOAD_FOLDER / file.filename
    file.save(save_path)
    return f"Received {file.filename}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
