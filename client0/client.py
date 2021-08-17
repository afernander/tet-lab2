
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
    while command_to_send != constants.QUIT_CODE:
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
        print('2) Generate a repayment table according to an interest rate.')
        print('3) Exit.')
        
        command_to_send = ''
        while(is_invalid_option(command_to_send, 1, 3)):
            command_to_send = input(': ')
        
        # Convert interest rates
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
            if (data_to_send == 'q'): continue

            while(not is_float(data_to_send)):
                print('Please, input a float number')
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            ir = float(data_to_send)

            # ACTUAL I.R. TYPE 
            print_convert_header(ir, actual_irt, new_irt)
            print('\nChoose the actual interest rate type (enter \'q\' to quit)')
            print('1) EM')
            print('2) EA')
            print('3) NMV')
            print('4) NAV')
            data_to_send = input(': ')
            if (data_to_send == 'q'): continue

            while(is_invalid_option(data_to_send, 1, 4)):
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            actual_irt = ir_types[int(data_to_send) - 1]

            # NEW I.R. TYPE 
            print_convert_header(ir, actual_irt, new_irt)
            print('\nChoose the target interest rate type (enter \'q\' to quit)')
            print('1) EM')
            print('2) EA')
            print('3) NMV')
            print('4) NAV')
            data_to_send = input(': ')
            if (data_to_send == 'q'): continue

            while(is_invalid_option(data_to_send, 1, 4)):
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            new_irt = ir_types[int(data_to_send) - 1]

            print_convert_header(ir, actual_irt, new_irt)

            command_and_data_to_send = f'{constants.CONVERT} {ir} {actual_irt} {new_irt}'
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            
            # ANSWER
            answer = data_received.decode(constants.ENCODING_FORMAT).split('\n')[1]
            print('\nAnswer')
            print(f': {answer} % {new_irt}')

            command_and_data_to_send = constants.QUIT
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print('\nPress any key to go back...')
            input()
        
        # Generate a repayment table according to an interest rate
        elif (command_to_send == constants.TABLE_CODE):
            # Connection
            client_socket.connect((constants.TABLE_SERVER, constants.TABLE_PORT))
            # local_tuple = client_socket.getsockname()
            
            # Starting...
            init_value = 0
            ir = 0
            months = 0
            print_gen_table_header(init_value, ir, months)

            # INITIAL CAPITAL
            print('\nSet the initial capital to borrow (enter \'q\' to quit)')
            data_to_send = input(': ')
            if (data_to_send == 'q'): continue

            while(not is_float(data_to_send)):
                print('Please, input a float number')
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            init_value = float(data_to_send)

            # INTEREST RATE
            print_gen_table_header(init_value, ir, months)
            print('\nInput the interest rate value (enter \'q\' to quit)')
            data_to_send = input(': ')
            if (data_to_send == 'q'): continue

            while(not is_float(data_to_send)):
                print('Please, input a float number')
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            ir = float(data_to_send)

            # MONTHS
            print_gen_table_header(init_value, ir, months)
            print('\nSet the periods amount to pay (enter \'q\' to quit)')
            data_to_send = input(': ')
            if (data_to_send == 'q'): continue

            while(not is_float(data_to_send)):
                data_to_send = input(': ')
                if (data_to_send == 'q'): break
            if (data_to_send == 'q'): continue

            months = int(data_to_send)

            print_gen_table_header(init_value, ir, months)

            command_and_data_to_send = f'{constants.TABLE} {init_value} {ir} {months}'
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            
            # ANSWER
            answer = data_received.decode(constants.ENCODING_FORMAT).split('\n')[1:]
            print('\nAnswer')
            for s in answer: print(s)

            command_and_data_to_send = constants.QUIT
            client_socket.send(command_and_data_to_send.encode(constants.ENCODING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)
            print('\nPress any key to go back...')
            input()
        client_socket.close() 
    
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

def print_gen_table_header(init_value, ir, months):
    os.system('clear')
    print(f'''IR Calculator Team present...
  ____ _____ _   _     _____  _    ____  _     _____ 
 / ___| ____| \ | |   |_   _|/ \  | __ )| |   | ____|
| |  _|  _| |  \| |_____| | / _ \ |  _ \| |   |  _|  
| |_| | |___| |\  |_____| |/ ___ \| |_) | |___| |___ 
 \____|_____|_| \_|     |_/_/   \_|____/|_____|_____|
Amount: {init_value:>,} $\t I. rate: {ir:.1f} % EM\t Periods: {months} months''')
    


if __name__ == '__main__':
    main()