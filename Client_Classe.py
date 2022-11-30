import socket 

class action:

    def __init__(self,host,port):
        self.host = host #  hôte visé par le client
        self.port = port # port visé par le client

    def connexion(self):
        client_socket = socket.socket()
        try: 
            client_socket.connect((self.host, self.port))  # connect to the server
            return(1)
        except socket.timeout as erreur:
            print("Délai de connexion dépassé")
            return(0)
        except Exception as e:
            print(f"Connexion impossible: {e}")
            return(0)

    def ping(self):
        client_socket = socket.socket()
        message = "ping"
        client_socket.send(message.encode())  # send message
        self.data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + self.data)  # show in terminal

        message = input(" -> ")  # again take input
        if self.data == "pong":
            return(1)
        else:
            return(0)