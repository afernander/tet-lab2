# ********************************************************************************************
    # Lab: Introduction to sockets
    # Course: ST0255 - Telemática
    # MultiThread TCP-SocketServer
# ********************************************************************************************

# Import libraries for networking communication and concurrency...

import socket
import threading
import constants

# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    server_execution()
    
# Handler for manage incomming clients conections...

def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
        remote_string = str(data_recevived.decode(constants.ENCONDING_FORMAT))
        remote_command = remote_string.split()
        command = remote_command[0]
        print (f'Data received from: {client_address[0]}:{client_address[1]}')

        
        if (command == constants.HELO):
            response = '100 OK\n'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
        elif (command == constants.QUIT):
            response = '200 BYE\n'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
            is_connected = False
        elif (command == constants.CIR):
            partial_response = change_ir(remote_command)
            response = str(round(partial_response, 2)) + "%\n300 DRCV\n"
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
        else:
            response = '400 BCMD\n\rCommand-Description: Bad command\n\r'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()


def change_ir(remote_command):
    print(remote_command)
    if(len(remote_command) < 3):
        return "Missing arguments"
    elif(remote_command[2] == "EM" and remote_command[3] == "EA"):
        return (((1+(float(remote_command[1])/100))**12) - 1) * 100
    elif(remote_command[2] == "EM" and remote_command[3] == "NMV"):
        return float(remote_command[1])*12
    elif(remote_command[2] == "EM" and remote_command[3] == "NAV"):
        return (((1+(float(remote_command[1])/100))**12)-1)*100
    elif(remote_command[2] == "EA" and remote_command[3] == "EM"):
        return (((1+(float(remote_command[1])/100))**(1/12)) - 1) * 100
    elif (remote_command[2] == "EA" and remote_command[3] == "NMV"):
        return  (((1+(float(remote_command[1])/100))**(1/12)) - 1) * 12 * 100
    elif (remote_command[2] == "EA" and remote_command[3] == "NAV"):
        return  remote_command[1]
    elif (remote_command[2] == "NMV" and remote_command[3] == "EM"):
        return float(remote_command[1])/12
    elif (remote_command[2] == "NMV" and remote_command[3] == "EA"):
        return (((((float(remote_command[1])/100)/12) + 1)**12) - 1) * 100
    elif (remote_command[2] == "NMV" and remote_command[3] == "NAV"):
        return (((((float(remote_command[1])/100)/12) + 1)**12) - 1) * 100
    elif (remote_command[2] == "NAV" and remote_command[3] == "EM"):
        return ((((float(remote_command[1])/100) + 1)**(1/12)) - 1) * 100
    elif (remote_command[2] == "NAV" and remote_command[3] == "EA"):
        return remote_command[1]
    elif (remote_command[2] == "NAV" and remote_command[3] == "NMV"):
        return ((((float(remote_command[1])/100) + 1)**(1/12)) - 1) * 12 * 100


#Function to start server process...
def server_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ('Socket is bind to address and port...')
    server_socket.listen(5)
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))
        client_thread.start()
    print('Socket is closed...')
    server_socket.close()

if __name__ == "__main__":
    main()