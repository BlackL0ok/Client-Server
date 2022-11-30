import socket 

class action:

    def __init__(self,host,port):
        self.host = host #  hôte visé par le client
        self.port = port # port visé par le client
        self.client_socket = socket.socket()

    def connexion(self):
        try: 
            self.client_socket.connect((self.host, self.port))  # connect to the server
            return(1)
        except socket.timeout as erreur:
            print("Délai de connexion dépassé")
            return(0)
        finally:
            print("Connexion impossible")
            return(0)

        def ping(self):
            msg = "ping"
            self.client_socket.send(message.encode())  # send message
            self.data = client_socket.recv(1024).decode()  # receive response