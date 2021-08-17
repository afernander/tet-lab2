import constants

# Handler for manage incomming clients conections...
def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        data_recevived = client_connection.recv(constants.RECV_BUFFER_SIZE)
        remote_string = str(data_recevived.decode(constants.ENCODING_FORMAT))
        remote_command = remote_string.split()
        print (f'Data received from: {client_address[0]}:{client_address[1]}')

        if (len(remote_command) == 0):
            continue

        command = remote_command[0]

        # Command ping
        if (command == constants.PING):
            response = '100 OK\n'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        # Command exit
        elif (command == constants.QUIT):
            response = '200 BYE\n'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
            is_connected = False
        # Command help
        elif (command == constants.HELP):
            response = '100 OK\nWelcome to Interest Rate Conversion Server!\nAvailable commands: help, ping, convert, exit\n\r'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        # Command convert
        elif (command == constants.CIR):
            if (len(remote_command) < 4):
                response = f'410 MARG\n\rMissing arguments: convert <value_%> <actual_irt> <new_irt>\n\r'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
                continue
            error_code = verify_arguments(remote_command[1], remote_command[2], remote_command[3])
            if (error_code > 0):
                response = f'42{error_code} IARG\n\rInvalid arguments\n401=value_%, 402=actual_irt, 403=new_irt\n\r'
                client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
                continue
            partial_response = change_ir(remote_command)
            response = '100 OK\n\r' + str(round(partial_response, 2)) + '\n\r'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
        else:
            response = f'400 BCMD\n\rCommand-Description: Unknown command "{command}"\n\r'
            client_connection.sendall(response.encode(constants.ENCODING_FORMAT))
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

def verify_arguments(val, actual_irt, new_irt):
    try:
        float(val)
    except ValueError:
        return 1
    
    try:
        str(actual_irt)
    except ValueError:
        return 2
    
    try:
        str(new_irt)
    except ValueError:
        return 3

    return 0

def change_ir(remote_command):
    value = float(remote_command[1])
    actual_irt = remote_command[2]
    new_irt = remote_command[3]

    if(actual_irt == "EM" and new_irt == "EA"):
        return (((1+(value/100))**12) - 1) * 100
    elif(actual_irt == "EM" and new_irt == "NMV"):
        return value*12
    elif(actual_irt == "EM" and new_irt == "NAV"):
        return (((1+(value/100))**12)-1)*100
    elif(actual_irt == "EA" and new_irt == "EM"):
        return (((1+(value/100))**(1/12)) - 1) * 100
    elif (actual_irt == "EA" and new_irt == "NMV"):
        return (((1+(value/100))**(1/12)) - 1) * 12 * 100
    elif (actual_irt == "EA" and new_irt == "NAV"):
        return value
    elif (actual_irt == "NMV" and new_irt == "EM"):
        return value/12
    elif (actual_irt == "NMV" and new_irt == "EA"):
        return (((((value/100)/12) + 1)**12) - 1) * 100
    elif (actual_irt == "NMV" and new_irt == "NAV"):
        return (((((value/100)/12) + 1)**12) - 1) * 100
    elif (actual_irt == "NAV" and new_irt == "EM"):
        return ((((value/100) + 1)**(1/12)) - 1) * 100
    elif (actual_irt == "NAV" and new_irt == "EA"):
        return value
    elif (actual_irt == "NAV" and new_irt == "NMV"):
        return ((((value/100) + 1)**(1/12)) - 1) * 12 * 100
