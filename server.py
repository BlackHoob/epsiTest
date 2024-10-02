
import socket
import select

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host,port = "127.0.0.1", 4000
serveur.bind((host,port))
serveur.listen(4)
client_connecte = True
socket_objs = [serveur]

print("Bienvenue dans le chat")

while client_connecte:

    liste_lu, liste_acce_Ecrit, exception = select.select(socket_objs, [], socket_objs)

    for socket_obj in liste_lu:
         
         if socket_obj is serveur:
              client, adresse = serveur.accept()
              print(f"l'object client socket: {client} - adresse: {adresse}")
              socket_objs.append(client)

else:
    donnees_recus = socket_obj.recv(128).decode("utf-8")

    if donnees_recus :
        print(donnees_recus)
    
    else:
        socket_objs.remove(socket_obj)
        print("1 participant est deconnecte")
        print(f"{len(socket_objs)-1} participants restants")
            













# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# PORT = 4000  # Port to listen on (non-privileged ports are > 1023)

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