# Microservice which converts characters or integers.
# This microservice will convert characters to hexadecimal for authentication key generation,
#   and convert Fahrenheit to Celsius
import time
import zmq  # For ZeroMQ

# @Context(): setup the environment to begin socket creation
context = zmq.Context()

# @socket(socket_type): This is the type of socket
#   we will be working with.  REP is a reply socket
socket = context.socket(zmq.REP)

# @bind(addr): This is the address string where the socket
#   will listen on the network port. Port number = 5555
socket.bind("tcp://*:5555")

# Create infinite loop that will wait for a message from the client.
while True:
    print("\nListening.")
    # Message from the client
    # @recv(flags=0, copy: bool=True, track: bool=False): will receive a message from the client.
    # This will be blank since we wait for message to arrive
    message = socket.recv()

    # contain hex value
    hexConversion = ''
    # convertor logic
    if len(message) != 1:
        for ch in message:
            hexConversion += hex(ch)
        socket.send_string(hexConversion)

    # We will decode the message so that we don't get a 'b' in front of text.  
    # ZeroMQ defaults to UTF-8 encoding when nothing is specified
    print(f"Received request from the client: {message.decode()}")

    if len(message) > 0:
        if message.decode() == 'Q': # Client asked server to quit
            break

        # Make the program sleep for X seconds
        time.sleep(3)

# Make a clean exit
print("\nProcess Killed.")
context.destroy()
