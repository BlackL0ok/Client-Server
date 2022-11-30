from Client_Classe import *
"""#
def client_program():
    client_socket = socket.socket()  # instantiate

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

"""

if __name__ == '__main__':
    action = action("193.32.126.225" ,55032)
    if action.connexion() == True:
        action.ping()