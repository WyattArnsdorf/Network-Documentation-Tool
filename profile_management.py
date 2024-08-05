import time
import zmq
import json

#Initialized dictionary for user database
user_profile_database = {
    "Wyatt": {
        "hex_key": "0x480x760x310x320x330x340x350x360x37",
        "data": ["wyatt@gmail.com", "2024", "admin"]
    }
}

#***************************************************************************# 
# Type: Helper Function
# Function Name: Process User Sign Up
# Description: processes a users sign up information to add it into the system as long
#              as a user doesn't currently have the same user ID
# Parameters: request_payload
# Returns: json.dumps()
#
#***************************************************************************#
def process_user_sign_up(request_payload):
    #load the json payload into usable variables
    request = json.loads(request_payload)
    user_id = request.get("user_id", "default_value")
    hex_key = request.get("hex_key", "default_value")
    email = request.get("email", "default_value")
    year = request.get("year", "default_value")
    role = request.get("role", "default_value")

    if user_id in user_profile_database:
        return json.dumps({"error": "Username already exists"})
    
    else:
        user_profile_database[user_id] = {
        "hex_key": hex_key,
        "data": [email, year, role]
        }
        
        return json.dumps({"message": "Successful. Please Login"})


#***************************************************************************# 
# Type: Helper Function
# Function Name: Process User Login
# Description: processes a users login information to verify there access into the system
# Parameters: request_payload
# Returns: json.dumps()
#
#***************************************************************************#
def process_user_login(request_payload):
    #load the json payload into usable variables
    request = json.loads(request_payload)
    user_id = request.get("user_id", "default_value")
    hex_key = request.get("hex_key", "default_value")

    if user_id in user_profile_database:
        if user_profile_database[user_id]["hex_key"] == hex_key:
            #Return user data as JSON string
            return json.dumps(user_profile_database[user_id]["data"])
        else:
            #Return error message as JSON string
            return json.dumps({"error": "Invalid hexadecimal key"})
    else:
        #Return error message as JSON string
        return json.dumps({"error": "Username not found"})


#initiate the socket context to wait for a reply from the client and run the main operations of the service
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")

while True:
    #Listen for request
    print("\nListening.") 
    load_request = socket.recv_string()

    #Process the request if its an actual payload
    if len(load_request) > 0:
        #receive the load to extrapilate the action required to preform
        true_request = json.loads(load_request)
        action = true_request.get("action")
        #If the action is to kill the server
        if action == 'Q':
            print("\nProcess Killed.")
            context.destroy()
            break
        #if the action is to login
        elif action == 'Login':
            response = process_user_login(load_request)
            #send the response back to the client
            socket.send_string(response)
        #if the action is to sign up
        elif action == 'Sign Up':
            response = process_user_sign_up(load_request)
            #send the response back to the client
            socket.send_string(response)

    time.sleep(3)
