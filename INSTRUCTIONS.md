Instructions on implementation:

Starting from the main program, you will need to set up a connection through zeroMQ using the "tcp://localhost:6666" port. In main.py: def login operations & def send_request are the primary drivers of the microservice from mains side. All that really needs to be established is the connection, the payload ,and the contents of the payload. The payload consists of a few fields of information for login and sign-up services. It's the method I used to take dictionary entries and convert them to json packages to be sent through the socket to then be re-assembled on the microservice side.  The most important field of the payload is the “action” variable which will tell the server the service being provided (Login, Sign-Up, Kill Program). The rest of the parameters/contents of the payload are general information based on the action being requested (i.e. Login service provides the user_id and hex_key and leaves all other fields empty/Sign-Up requires all the fields provided [either by the program or the user] to give the “database” the users information from the system). If you want to use the def send_request function from my main program feel free to.

Step-by-Step:

1. setup request connection using zeroMQ "tcp://localhost:6666"

2. create function to deliver a json payload in dictionary format. See "def send_request()" within "main.py" as an example

3. provide the payload with the desired information to send to the server. action, user_id and password_key for login; action, user_id, password_key, email, year and role for sign up.

4. send the payload using socket.send_string(json.dumps("dictionary string")) to send it using the json library.

5. receive the payload using socket.recv_string() and then use json.loads("response dictionary string") to convert it back from json to usable dictionary/string format


Important:

The server is based on the key generation from the convertor microservice. As long as you use the service to generate the key, then it should be able to validate that key generated from converterMicroservice.py.

In Main Program:

Def login_operations()

Def send_request(action, user_id, hex_key, email, year, role)

In Profile Management Service:

Def process_user_sign_up(request_payload)

Def process_user_login(request_payload):
