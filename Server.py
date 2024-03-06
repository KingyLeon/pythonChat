import socket
import sys
import time

# Creating the server
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

# Incoming connection
new_socket.bind((host_name, port))
print("Binding complete")
print("Your IP is:", s_ip)

# Listen to user input
name = input('Enter name:')
new_socket.listen(1)

# Accept incoming connection
conn, add = new_socket.accept()
print("Received connection from, add[]")
print('Connection Established. Connected From: ', add[0])

# Storing Incoming connecton data
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())

# Open file history

while True:
    f = open('History.txt', 'a')
    message = input('Me: ')
    f.write(message + "\n")
    f.close()
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    f = open('History.txt', 'a')
    f.write(message + "\n")
    print(client, ':', message)
    f.close()

    