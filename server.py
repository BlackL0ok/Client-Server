# coding: utf-8

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 55032))

print("En Écoute...")
while True:
        socket.listen(5)
        client, address = socket.accept()
        print ("{} connected".format( address ))

        response = client.recv(255)
        if response != "":
                print (response)

print ("Close")
client.close()
stock.close()