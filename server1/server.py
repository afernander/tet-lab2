#Code based on https://github.com/ST0263/st0263-20212/blob/main/LabSocketsMultiThread/ServerLab.py

#!/usr/bin/env python3
import socket
import threading

import constants
import connection

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER

def main():
    print("***********************************")
    print("Server is running (", server_address, ":", constants.PORT, ")...")
    server_execution()

#Function to start server process...
def server_execution():
    tuple_connection = (server_address, constants.PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=connection.handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    print('Socket is closed...')
    server_socket.close()

if __name__ == "__main__":
    main()