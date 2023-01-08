import socket

class action:

    def __init__(self,host,port):
        self.host = host #  hôte visé par le client
        self.port = port # port visé par le client
        self.client_socket = socket.socket()

    def connexion(self):
        try: 
            self.client_socket.connect((self.host, self.port))  # connect to the server
            message = "ping"
            for k in range(4):
                self.client_socket.send(message.encode())  # send message
                data = self.client_socket.recv(1024).decode()  # receive response
                if data == "pong":
                    print("Connexion: ok")
                    return(1)
            print("Erreur lors de dialogiue")
            return(0)
        except socket.timeout as erreur:
            print("Délai de connexion dépassé")
            return(0)
        except Exception as e:
            print(f"Connexion impossible: {e}")
            return(0)

    def send(self,text):
        self.client_socket = socket.socket()
        self.client_socket.connect((self.host, self.port))  # connect to the server
        text_string = text[0].encode() +"#/#".encode() + text[1].encode()
        self.client_socket.send(text_string)  # send message
        print(text_string)
