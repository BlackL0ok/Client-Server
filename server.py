import socket, os
from  Server_Classe import Sql as sql

def server_program():
    # get the hostname
    host = "0.0.0.0" #socket.gethostname()
    port = 55264  # initiate port no above 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    print("En attente d'une connection...")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data: break;
        print("from connected user: " + str(data))
        if data == "ping":
            msg = "pong"
            conn.send(msg.encode())  # send data to the client
            print("Connection seems to be good !")
        elif not data: break;

    conn.close()  # close the connection


if __name__ == '__main__':
    sql = sql("databank")
    if os.path.exists("databank"):
        print("Création")
        sql.create_file("databank")
        column_table_login_user = [("id","integer PRIMARY KEY AUTOINCREMENT"),("User","text"),("Password","text")]
        sql.create_table("login_user",column_table_login_user)
        column_table_user_data = [("id","integer PRIMARY KEY AUTOINCREMENT"),("User","text"),("Password","text"),("Description","text"),("Right","integer")]
        sql.create_table("User_data",column_table_user_data)
        
    server_program()
