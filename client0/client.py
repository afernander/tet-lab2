
import socket
import constants

def main():
    print('***********************************')
    print('Client is running...')
    """
    client_socket.connect(("127.0.0.1",constants.PORT))
    local_tuple = client_socket.getsockname()
    print('Connected to the server from:', local_tuple)
    """
    command_to_send = ""
    while command_to_send != constants.QUIT:
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print('Enter \"QUIT\" to exit')
        print('Enter \"CONVERT\" to convert interest rates')
        print('Enter \"TABLE\" to visualize a payments table according to your interest rate')
        print('Input commands:')
        command_to_send = input()
        if command_to_send == '':
            print('\nPlease input a valid command... \n')       
        elif (command_to_send == constants.CONVERT):
            client_socket.connect(("127.0.0.1", constants.CONVERT_PORT))
            local_tuple = client_socket.getsockname()
            print('Connected to the server from:', local_tuple)
            
            data_to_send = input('Input data to send: ') 
            command_and_data_to_send = command_to_send + ' ' + data_to_send
            client_socket.send(bytes(command_and_data_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))

            command_and_data_to_send = constants.QUIT
            client_socket.send(bytes(command_and_data_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)  
        elif (command_to_send == constants.TABLE):
            client_socket.connect(("127.0.0.1", constants.TABLE_PORT))
            local_tuple = client_socket.getsockname()
            print('Connected to the server from:', local_tuple)
            
            data_to_send = input('Input data to send: ') 
            command_and_data_to_send = "CIR" + ' ' + data_to_send
            client_socket.send(bytes(command_and_data_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))

            command_and_data_to_send = constants.QUIT
            client_socket.send(bytes(command_and_data_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)  
        else:        
            client_socket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))
        client_socket.close()   
    
    client_socket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
    print(data_received.decode(constants.ENCONDING_FORMAT))
    print('Closing connection...BYE BYE...') 
    
if __name__ == '__main__':
    main()