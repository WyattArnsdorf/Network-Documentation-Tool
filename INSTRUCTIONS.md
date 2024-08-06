Instructions on implementation:

Starting from the main program, you will need to set up a connection through zeroMQ using the "tcp://localhost:6666" port. In main.py: def login operations & def send_request are the primary drivers of the microservice from mains side. All that really needs to be established is the connection, the payload ,and the contents of the payload. The payload consists of a few fields of information for login and sign-up services. It's the method I used to take dictionary entries and convert them to json packages to be sent through the socket to then be re-assembled on the microservice side.  The most important field of the payload is the “action” variable which will tell the server the service being provided (Login, Sign-Up, Kill Program). The rest of the parameters/contents of the payload are general information based on the action being requested (i.e. Login service provides the user_id and hex_key and leaves all other fields empty/Sign-Up requires all the fields provided [either by the program or the user] to give the “database” the users information from the system). If you want to use the def send_request function from my main program feel free to.

Important:
The server is based on the key generation from the convertor microservice. As long as you use the service to generate the key, then it should be able to validate that key generated from converterMicroservice.py.

In Main Program:
Def login_operations()
Def send_request(action, user_id, hex_key, email, year, role)

In Profile Management Service:
Def process_user_sign_up(request_payload)
Def process_user_login(request_payload):
