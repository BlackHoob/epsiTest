
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host,port = "127.0.0.1", 4000
client_socket.connect((host,port))
nom = input("Quelle est votre nom ?")

if __name__ =="__main__":

    while True:

        message = input(f"{nom} > ")
        client_socket.send(f"{nom} > {message}".encode("utf-8")) # La méthode send pour envoyer les infos du client au serveur et la methode encode pour encoder en bite


























# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)

# print(f"Received {data!r}")

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)