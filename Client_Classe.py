import socket 

class action:

    def __init__(self,host,port):
        self.host = host #  hôte visé par le client
        self.port = port # port visé par le client
        try: 
            client_socket = socket.socket()  # instantiate
            client_socket.connect((self.host, self.port))  # connect to the server
            return(1)
        except socket.timeout as erreur:
            print("Délai de connexion dépassé")
            return(0)
        finally:
            print("Connexion impossible")
            return(0)