import sqlite3, socket, os, rsa

class Sql:
    def __init__(self,name_file):
        self.sql3 = sqlite3.connect(f"{name_file}")
        self.cursor = self.sql3.cursor()
        self.publicKey, self.privateKey = rsa.newkeys(512)
        
    def create_file(self,name_file):
        try:
            sqlite3.connect(f"{name_file}")
            return(True)
        except Exception as e:
            print(f"Erreur (connection): {e}")
            return(False)

    def create_table(self,name_table,liste_column): # liste_column est une liste de tuple avec nom de la column et type (en str)
        try:
            x = 0
            liste_column_text = ""
            for k in range(len(liste_column)-1):
                liste_column_text += f"{liste_column[k][0]} {liste_column[k][1]}, "
                x += 1
            liste_column_text += f"{liste_column[x][0]} {liste_column[x][1]}"
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {name_table} ({liste_column_text})")
            return(True)
        except Exception as e:
            print(f"Erreur (création table)- {e}")
            return(False)

    def insert_data(self,name_table,name_column,value):
        try:
            name_column = "".join(name_column)
            value = "".join(value)
            request = f"INSERT INTO {name_table}(" + name_column +") VALUES ("+ value+");"
            self.cursor.execute(request)
            self.sql3.commit()
        except Exception as e:
            print(f"Erreur (insert_data)- {e}")
            return(False)
    
    def check_login(self):
        self.request_userPswd = """SELECT User,Password FROM login_user;"""
        self.list_user = list(self.cursor.execute(self.request_userPswd))
        print(self.list_user)

class Server_outils():

    def check_if_login(self,address,conn):
        client_socket = socket.socket()
        message = "ping"
        client_socket.send(message.encode())  # send message
        # receive data stream. it won't accept data packet greater than 1024 bytes
        
        while True:
            data = conn.recv(1024).decode()
            if not data: test_msg += 1;
            elif data == "pong":
                msg = "ok"
                conn.send(msg.encode())  # send data to the client
                print("Connection from: " + str(address))
            elif test_msg < 3 :
                break
        print("Erreur lors du ping")
