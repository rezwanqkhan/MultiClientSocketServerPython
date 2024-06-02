import socket


def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))

    # listen for incoming connections
    server.listen()
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # receive data from the client
    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8")  # convert bytes to string

        # check if the received message is "close"
        if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
            client_socket.send("closed".encode("utf-8"))
            break

        # split the received message by "+" and calculate the sum
        numbers = request.split("+")
        total = sum(int(num) for num in numbers)

        print(f"Received: {request}, Sum: {total}")
        response = str(total).encode("utf-8")  # convert integer total to bytes

        # send the sum back to the client
        client_socket.send(response)

    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")

    # close server socket
    server.close()


run_server()
