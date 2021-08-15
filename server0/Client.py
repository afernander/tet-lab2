# ********************************************************************************************
    # Lab: Introduction to sockets
    # Course: ST0255 - Telemática
    # TCP-Socket Client
# ********************************************************************************************

#Import libraries for networking communication...


import socket
import constants

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
    print('***********************************')
    print('Client is running...')
    client_socket.connect(("127.0.0.1",constants.PORT))
    local_tuple = client_socket.getsockname()
    print('Connected to the server from:', local_tuple)
    print('Enter \"quit\" to exit')
    print('Input commands:')
    complete_command = input()
    print(complete_command)
    
    while complete_command != constants.QUIT:
        if complete_command == '':
            print('Please input a valid command...')
            complete_command = input()                        
        elif (complete_command == constants.DATA):
            data_to_send = input('Input data to send: ') 
            command_and_data_to_send = complete_command + ' ' + data_to_send
            client_socket.send(bytes(command_and_data_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))
            complete_command = input()            
        else:      
            client_socket.send(bytes(complete_command,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))
            complete_command = input()
    
    client_socket.send(bytes(complete_command,constants.ENCONDING_FORMAT))
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
    print(data_received.decode(constants.ENCONDING_FORMAT))
    print('Closing connection...BYE BYE...')
    client_socket.close()    

if __name__ == '__main__':
    main()