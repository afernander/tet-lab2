
import os
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
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        os.system('clear')
        print('Welcome to IR Calculator v1.0!')
        print('''
            ________     ______      __           __      __            
           /  _/ __ \   / ____/___ _/ /______  __/ /___ _/ /_____  _____
           / // /_/ /  / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
         _/ // _, _/  / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
        /___/_/ |_|   \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
        ''')

        print('Select the option:')
        print('1) Convert interest rates.')
        print('2) Visualize a payments table according to your interest rate.')
        print('3) Exit.')
        
        command_to_send = ''
        while(is_invalid_option(command_to_send, 1, 3)):
            command_to_send = input(': ')
        
        if (command_to_send == constants.CONVERT_CODE):
            # Connection
            client_socket.connect((constants.CONVERT_SERVER, constants.CONVERT_PORT))
            # local_tuple = client_socket.getsockname()
            
            # Starting...
            ir = 0
            actual_irt = '-'
            new_irt = '-'
            ir_types = ['EM', 'EA', 'NMV', 'NAV']
            print_convert_header(ir, actual_irt, new_irt)

            # INTEREST RATE
            print('\nInput the interest rate value (enter \'q\' to quit)')
            data_to_send = input(': ')
            if (data_to_send == 'q'): break

            while(not is_float(data_to_send)):
                print('Please, input a float number')
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): break

            ir = float(data_to_send)

            # ACTUAL I.R. TYPE 
            print_convert_header(ir, actual_irt, new_irt)
            print('\nChoose the actual interest rate type (enter \'q\' to quit)')
            print('1) EM')
            print('2) EA')
            print('3) NMV')
            print('4) NAV')
            data_to_send = input(': ')
            if (data_to_send == 'q'): break

            while(is_invalid_option(data_to_send, 1, 4)):
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): break

            actual_irt = ir_types[int(data_to_send) - 1]

            # NEW I.R. TYPE 
            print_convert_header(ir, actual_irt, new_irt)
            print('\nChoose the target interest rate type (enter \'q\' to quit)')
            print('1) EM')
            print('2) EA')
            print('3) NMV')
            print('4) NAV')
            data_to_send = input(': ')
            if (data_to_send == 'q'): break

            while(is_invalid_option(data_to_send, 1, 4)):
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): break

            new_irt = ir_types[int(data_to_send) - 1]

            print_convert_header(ir, actual_irt, new_irt)

            command_and_data_to_send = f'{constants.CONVERT} {ir} {actual_irt} {new_irt}'
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            
            # ANSWER
            answer = data_received.decode(constants.ENCODING_FORMAT).split("\n")[1]
            print('Answer')
            print(f': {answer} % {new_irt}')

            command_and_data_to_send = constants.QUIT
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print('\nPress any key to go back...')
            input()
        
        elif (command_to_send == constants.TABLE):
            client_socket.connect(("127.0.0.1", constants.TABLE_PORT))
            local_tuple = client_socket.getsockname()
            print('Connected to the server from:', local_tuple)
            
            data_to_send = input('Input data to send: ') 
            command_and_data_to_send = command_to_send + ' ' + data_to_send
            client_socket.send(bytes(command_and_data_to_send,constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCODING_FORMAT))

            command_and_data_to_send = constants.QUIT
            client_socket.send(bytes(command_and_data_to_send,constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)  
        else:        
            print('\nPlease input a valid command... \n')  
        client_socket.close()   
    
    client_socket.send(bytes(command_to_send,constants.ENCODING_FORMAT))
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
    print(data_received.decode(constants.ENCODING_FORMAT))
    print('Closing connection...BYE BYE...') 
    
def is_invalid_option(menu, init_op, final_op):
    try:
        menu = int(menu)
        if (menu < init_op or menu > final_op):
            print('Choose a valid option')
            return True
        return False
    
    except ValueError:
        if (menu != ''):
            print('Choose a valid option')
        return True

def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def print_convert_header(ir, actual_irt, new_irt):
    os.system('clear')
    print(f'''IR Calculator Team present...
   ___ ___  _  ___   _____ ___ _____ ___ ___ 
  / __/ _ \| \| \ \ / / __| _ \_   _| __| _ \\
 | (_| (_) | .` |\ V /| _||   / | | | _||   /
  \___\___/|_|\_| \_/ |___|_|_\ |_| |___|_|_\\
I. rate: {ir:.1f} %\t\tActual type: {actual_irt}\t\tNew type: {new_irt}''')

if __name__ == '__main__':
    main()