import constants

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
