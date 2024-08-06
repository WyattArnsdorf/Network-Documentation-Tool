from device_inventory import Inventory
import time
import zmq
import json

####################################################Main#################################################
def main():
    authentication = '1'
    print("\nTest = 0. Continue = 1: ", end="")
    first_input = input()
    if first_input == '0':
        test_login_operations()
        establish_key('Q')
        send_request('Q')
        print("\nShutdown Successful. Goodbye.")

    elif first_input == '1':
        while True:
            if authentication == '1' or authentication == '0':
                authentication = login_operations()
                #If the user is verified
                if authentication == '1': 
                    print("\n")
                    print_ui("_Version_")

                    while True:
                        print("\n")
                        print_ui("Home")
                        print("\n")
                        print("Please enter option: ", end=" ")
                        user_input = input().strip()
                        #Access the inventory documents
                        if user_input == "1":
                            inventory_object = Inventory()
                            inventory_object.main_inventory()

                        #elif user_input == "2":
                            #section = "_Configuration Files_"

                        #quit the main program
                        elif user_input == "Q" or user_input == "q":
                            authentication = '2'
                            break
                #If the user cannot be verified
                elif authentication == '0':
                    print("\nUnable to authenticate. Please try again: ")

            else:
                #Quit Program
                establish_key('Q')
                send_request('Q')
                break


#################################################Functions##############################################

#***************************************************************************# 
# Type: Helper Function
# Function Name: Login Operations
# Description: Initiates and manages the login/sign-up process by prompting for their credentials
# Parameters: n/a
# Returns: returns result of login operations
#
#***************************************************************************#
def test_login_operations():
    print("\n")
    print_ui("_Login_")
    print("\nInitiating test protocol...")    
    time.sleep(2)

    print("\nBeginning Sign Up Sequence...")
    time.sleep(2)

    print("\nIf you have an account, login. If you are not registered, signup. ")
    print("\nPlease enter option: ", end="")
    time.sleep(1)
    print("2")
    print("\nPlease enter your user ID: ", end="")
    time.sleep(1)
    print("Jennifer")
    id = "Jennifer"
    print("\nPlease enter your Password: ", end="")
    time.sleep(1)
    print("rainbowSherbert42")
    password = "rainbowSherbert42"
    #takes the provided password and turns it into a usable key
    password_key = establish_key(password)
    print("\nPlease enter your email: ", end="")
    time.sleep(1)
    print("jennifer@hotmail.com")
    email = "jennifer@hotmail.com"
    print("\nPlease enter your role (""admin"", ""user""): ", end="")
    time.sleep(1)
    print("user")
    role = "user"
    send_request("Sign Up", id, password_key, email, "2024", role)
    print("\nSuccessful. Please Login")

    print("Beginning Login Sequence...")
    time.sleep(3)

    print("\nIf you have an account, login. If you are not registered, signup. ")
    print("\nPlease enter option: ", end="")
    time.sleep(1)
    print("1")
    print("\nPlease enter your user ID: ", end="")
    time.sleep(1)
    print("Jennifer")
    id = "Jennifer"
    print("\nPlease enter your Password: ", end="")
    time.sleep(1)
    print("rainbowSherbert42")
    password = "rainbowSherbert42"
    #takes the provided password and turns it into a usable key
    password_key = establish_key(password)
    response_data = send_request("Login", id, password_key)
    print(f"Successful! Received: {response_data}")
    
    print("\nInitiating Program Shutdown...")
    time.sleep(2)

#***************************************************************************# 
# Type: Helper Function
# Function Name: Login Operations
# Description: Initiates and manages the login/sign-up process by prompting for their credentials
# Parameters: n/a
# Returns: returns result of login operations
#
#***************************************************************************#
def login_operations():
    print("\n")
    print_ui("_Login_")
    authentication = ''
    while True:
        print("\nIf you have an account, login. If you are not registered, signup. ")
        print("\nPlease enter option: ", end="")
        user_input = input()

        #Login
        if user_input == "1":
            #get user credentials
            print("\nPlease enter your user ID: ", end="")
            id = input()
            print("\nPlease enter your Password: ", end="")
            password = input()
            #establish the key
            password_key = establish_key(password)
            #use key and login ID to get response
            response_data = send_request("Login", id, password_key)
            if response_data == {"error": "Username not found"}:
                authentication = '0'
                return authentication
            
            else:
                authentication = '1'
                print(f"Received: {response_data}")
                return authentication
        #Sign Up
        elif user_input == "2":
            #get user credentials
            print("\nPlease enter your user ID: ", end="")
            id = input()
            print("\nPlease enter your Password: ", end="")
            password = input()
            #takes the provided password and turns it into a usable key
            password_key = establish_key(password)
            print("\nPlease enter your email: ", end="")
            email = input()
            print("\nPlease enter your role (""admin"", ""user""): ", end="")
            role = input()
            response_data = send_request("Sign Up", id, password_key, email, "2024", role)

            if response_data == {"error": "Username already exists"}:
                print("\nUsername already exists")

            else:
                print("\nSuccessful. Please Login")
                break

        #Quit program
        elif user_input == "Q" or user_input == "q":
            #returns "2" from both functions to kill the servers
            authentication = '2'
            return authentication 

        else:
            print("\nIncorrect option, please try again. ")


#***************************************************************************# 
# Type: Helper Function
# Function Name: Send Request
# Description: connects to the profile management service and creates a request payload to send to the 
#              server. The payload is a compilation of the requested actions as well as user info. Parameters 
#              with the "=None" are optional based on the requested action of the server. 
# Parameters: action, user_id, hex_key, email, year, role
# Returns: response_date
#
#***************************************************************************#
def send_request(action, user_id=None, hex_key=None, email=None, year=None, role=None):
    #establish the socket to the server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:6666")

    #complete the payload with the provided parameters
    request_payload = {
        "action": action,
        "user_id": user_id,
        "hex_key": hex_key,
        "email": email,
        "year": year,
        "role": role
    }
    #send payload
    socket.send_string(json.dumps(request_payload))
    #receive payload
    response = socket.recv_string()
    #convert payload from json to parsable string
    response_data = json.loads(response)
    
    context.destroy()
    return response_data

#***************************************************************************# 
# Type: Helper Function
# Function Name: Establish Key
# Description: connects to the convertor microservice to generate a key from the provided password
# Parameters: password
# Returns: hex_key
#
#***************************************************************************#
def establish_key(password):
    #initialize binding environment
    context = zmq.Context()
    #establish sicket type "REQ: request"
    socket = context.socket(zmq.REQ)
    #bind the socket using the correct protocol and port # 5555
    socket.connect("tcp://localhost:5555")

    if password == 'Q':
        #Kill server processing.
        socket.send_string('Q')
        return '2'
    
    else:
        #send msg through the socket
        socket.send_string(password)
        #get the hex_key from the server
        hex_key = socket.recv_string()

        context.destroy()
        return hex_key


#***************************************************************************# 
# Type: 
# Function Name:
# Description: 
# Parameters:
# Returns:
#
#***************************************************************************#
def print_ui(section_title):
    try:    
        file = open("UI/UI-Home.txt", 'r')
        in_section = False
        i = 0
        for line in file:
            if section_title in line:
                in_section = True

            if in_section:
                print(line, end="") 

                if line.strip().endswith("#"):
                    i += 1

                if i == 3: 
                    break
        
        file.close()

    except FileNotFoundError:
        print("File not found.")

#***************************************************************************# 
# Type: 
# Function Name:
# Description: 
# Parameters:
# Returns:
#
#***************************************************************************#

if __name__ == "__main__":
    main()
    
